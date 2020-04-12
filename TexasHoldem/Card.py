
suits = ["S", "C", "D", "H"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

pipRankings = {
	"2" : 1,
	"3" : 2,
	"4" : 3,
	"5": 4,
	"6": 5,
	"7": 6,
	"8" : 7,
	"9" : 8,
	"10" : 9,
	"J" : 10,
	"Q": 11,
	"K": 12,
	"A": 13
}

cardRankings = {
	'ROYAL_FLUSH' : 10,
	'QUADS' : 9,
	'STRAIGHT_FLUSH' : 8,
	'FULL_HOUSE' : 7,
	'FLUSH' : 6,
	'STRAIGHT' : 5,
	'TRIPS' : 4,
	'TWO_PAIR' : 3,
	'ONE_PAIR': 2,
	'HIGH_CARD' : 1
}


class Card:
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number

	def __str__(self):
		return f"{self.number}{self.suit.lower()}"

	def __lt__(self, other):
		return pipRankings[self.number] < pipRankings[other.number]

	def __le__(self, other):
		return pipRankings[self.number] <= pipRankings[other.number]

	def __gt__(self, other):
		return pipRankings[self.number] > pipRankings[other.number]

	def __ge__(self, other):
		return pipRankings[self.number] >= pipRankings[other.number]

	def __eq__(self, other):
		return pipRankings[self.number] == pipRankings[other.number]

	def __ne__(self, other):
		return pipRankings[self.number] != pipRankings[other.number]

	def is1Less(self, other):
		return pipRankings[other.number] - pipRankings[self.number] in [1, 12]
