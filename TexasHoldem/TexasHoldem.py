import random, queue, HandRanking, Card, Player, Table

table = Table.Table(6)

class TexasHoldem:
	def __init__(self, deck, table):
		self.players = queue.Queue(maxsize=100)
		self.table = table
		self.playersNotQueue = []
		self.deck = deck
		self.pot = 0
		self.comCards = []
		self.toCall = self.table.bigBlind

		self.actions = ["B", "R", "F", "Chk", "C"]

	def printYourHand(self, x):
		self.playersNotQueue[x].printPlayerHand()

	def isFinished(self):
		for player in self.playersNotQueue:
			if player.stack == 6000:
				return True
			if player.stack >= 0:
				return False
		return False

	def printComCards(self):
		print(" ".join([str(x) for x in self.comCards]))

	def addPlayers(self, players):
		for item in players:
			self.players.put(item)
		self.playersNotQueue = players

	def shuffleDeck(self):
		for x in range(5):
			random.shuffle(self.deck)

	def dealHand(self):
		self.shuffleDeck()
		for _ in range(2):
			for player in self.playersNotQueue[1:]:
				player.addCard(self.deck.pop())
			players[0].addCard(self.deck.pop())


	def burnCard(self):
		self.deck.pop()

	def toTheFlop(self):
		self.burnCard()
		for x in range(3):
			self.comCards.append(self.deck.pop())

	def toTheTurnOrRiver(self):
		self.burnCard()
		self.comCards.append(self.deck.pop())

	def preFlopOrder(self):
		btn = self.players.get()
		sb = self.players.get()
		bb = self.players.get()
		sb.stack -= self.table.smallBlind
		sb.chipsAlreadyIn = self.table.smallBlind
		bb.stack -= self.table.bigBlind
		bb.chipsAlreadyIn = self.table.bigBlind
		self.players.put(btn)
		self.players.put(sb)
		self.players.put(bb)
		self.pot += self.table.smallBlind + self.table.bigBlind

	def postFlopOrder(self):
		for player in self.playersNotQueue[1:]:
			if not player.folded:
				self.players.put(player)
		if not self.playersNotQueue[0].folded:
			self.players.put(self.playersNotQueue[0])

	def doAction(self, player, action = None):
		if action == None:
			action = "C"
		if action == "Chk":
			return
		if action == "F":
			player.folded = True
			return
		if action == "C":
			self.pot += (self.toCall - player.chipsAlreadyIn)
			player.stack -= (self.toCall - player.chipsAlreadyIn)
			player.chipsAlreadyIn = self.toCall
			return

	def getAction(self):
		action = input("""\nAction : ["B", "R", "F", "Chk", "C"]""")
		return action

	def bettingRound(self):
		while not self.players.empty():
			playerToAct = self.players.get()
			if playerToAct.isYou:
				self.doAction(playerToAct, "C")
			else:
				self.doAction(playerToAct)

	def printplayersandstacks(self):
		while not self.players.empty():
			p = self.players.get()
			print(p.number, p.stack)

	def getPlayerAndComHand(self, player):
		# Order players hand with the board
		handAndCom = player.hand + self.comCards
		handAndCom.sort()
		return handAndCom

	def getEquivHandRanking(self, hand):
		hr = HandRanking.HandRanking(hand)
		ranking = hr.analyzeRank()
		return ranking


	def checkWinner(self):
		currentBest = []
		for player in self.playersNotQueue:
			hand = self.getPlayerAndComHand(player)
			print(f"Player '{player.number}' has")
			print(" ".join([str(x) for x in hand]))
			print(self.getEquivHandRanking(hand))



cards = []
for suit in Card.suits:
	for number in Card.numbers:
		cards.append(Card.Card(suit, number))

players = []
yourPlayer = random.randint(1, 6)
for x in range(1, table.players + 1):
	players.append(Player.Player(x, yourPlayer == x, 1000))

game = TexasHoldem(cards, table)
game.addPlayers(players)

debug = False

while not game.isFinished() and not debug:
	game.dealHand()
	game.printYourHand(yourPlayer - 1)
	game.preFlopOrder()
	game.bettingRound()

	game.toTheFlop()
	game.printComCards()
	game.postFlopOrder()
	game.bettingRound()

	game.toTheTurnOrRiver()
	game.printComCards()
	game.postFlopOrder()
	game.bettingRound()

	game.toTheTurnOrRiver()
	game.printComCards()
	game.postFlopOrder()
	game.bettingRound()
	
	game.checkWinner()
	break
