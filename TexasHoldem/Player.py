class Player:
	def __init__(self, number, ai, startingStack):
		self.number = number
		self.hand = []
		self.stack = startingStack
		self.folded = False
		self.chipsAlreadyIn = 0
		self.isYou = ai

	def addCard(self, singleCard):
		self.hand.append(singleCard)

	def printPlayerHand(self):
		print(" ".join([str(x) for x in self.hand]))
