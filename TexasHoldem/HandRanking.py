import Card
class HandRanking:
	royalFlushes = [[Card.Card(Card.suits[z], Card.numbers[x]) for x in range(8, 13)] for z in range(4)]
	def __init__(self, cards):
		self.cards = cards

	def analyzeRank(self):
		"""Returns the rank of the players cards"""
		if self.isRoyal():
			return 'ROYAL_FLUSH'
		if self.isQuad():
			return 'QUADS'
		if self.isStraightFlush():
			return 'STRAIGHT_FLUSH'
		i = self.cards
		if self.isFullHouse():
			return 'FULL_HOUSE'
		self.cards = i
		if self.isFlush():
			return 'FLUSH'
		if self.isStraight():
			return 'STRAIGHT'
		if self.isTrips():
			return 'TRIPS'
		if self.isTwoPair():
			return 'TWO_PAIR'
		if self.isOnePair():
			return 'ONE_PAIR'
		return 'HIGH_CARD'

	def isRoyal(self):
		for item in self.royalFlushes:
			if self.cards[2:] != item:
				return False
		return True

	def isQuad(self):
		for x in range(0, 4):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 4):
				if x != y:
					checkCard = self.cards[y]
					if curCard.number != checkCard.number:
						allGood = False
						break
					else:
						allGood = True
			if allGood:
				return True
		return False

	def isStraightFlush(self):
		for x in range(0, 3):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 5):
				if x != y:
					checkCard = self.cards[y]
					if curCard.suit != checkCard.suit or not curCard.is1Less(checkCard):
						allGood = False
						break
					else:
						allGood = True
					curCard = self.cards[y]
			if allGood:
				return allGood
		return False

	def isFullHouse(self):
		x = self.isTrips(True)
		if x:
			return self.isOnePair(True)
		return False

	def isFlush(self):
		toCount = {Card.suits[x]: 0 for x in range(4)}
		for item in self.cards:
			toCount[item.suit] += 1
		for key, val in toCount.items():
			if val > 4:
				return True
		return False

	def isStraight(self):
		for x in range(0, 3):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 5):
				if x != y:
					checkCard = self.cards[y]
					if not curCard.is1Less(checkCard):
						allGood = False
						break
					else:
						allGood = True
					curCard = self.cards[y]
			if allGood:
				return True
		return False

	def isTrips(self, remove = False):
		for x in range(0, 5):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 3):
				if x != y:
					checkCard = self.cards[y]
					if curCard.number != checkCard.number:
						allGood = False
						break
					else:
						allGood = True
					curCard = self.cards[y]
			if allGood:
				if remove:
					new = self.cards[:x]+self.cards[y:]
					self.cards = new
				return True
		return False

	def isTwoPair(self):
		count = 0
		for x in range(0, 6):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 2):
				if x != y:
					checkCard = self.cards[y]
					if curCard.number != checkCard.number:
						allGood = False
						break
					else:
						allGood = True
					curCard = self.cards[y]
			if allGood:
				count += 1
		return count >= 2

	def isOnePair(self, removed = False):
		upper = 6
		if removed:
			upper = 3
		for x in range(0, upper):
			curCard = self.cards[x]
			allGood = False
			for y in range(x, x + 2):
				if x != y:
					checkCard = self.cards[y]
					if curCard.number != checkCard.number:
						allGood = False
						break
					else:
						allGood = True
					curCard = self.cards[y]
			if allGood:
				return True
		return False
