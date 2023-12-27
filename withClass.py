import collections

# Named tuple to represent a playing card
Card = collections.namedtuple('Card', ['rank', 'suit'])

class Deck:
# Use letters to represent suits: 'S' for Spades, 'H' for Hearts, 'D' for Diamonds, 'C' for Clubs
	suits = 'SHDC'
	ranks = '23456789TJQKA'
	def __init__(self):
	# Initialize the deck with all possible combinations of ranks and suits
		self.cards = [
		Card(rank, suit)
		for suit in self.suits
		for rank in self.ranks
		]
		# List to track dealt cards
		self.dealt_cards = []

	def __str__(self):
		# Provide a string representation of the deck for better visualization
		return f"Deck with {len(self.cards)} cards: {', '.join(map(str, self.cards))}"

	def deal(self):
		# Deal a card from the top of the deck (pop lets you select & remove the last item from a row)
		dealt_card = self.cards.pop()
		# Track the dealt card
		self.dealt_cards.append(dealt_card)
		return dealt_card

# Example usage:
deck = Deck()
print(deck) # Display the initial state of the deck

# Deal a card and display the updated deck
dealt_card = deck.deal()
print(f"Dealt card: {dealt_card}")
print(deck) # Display the updated state of the deck after dealing a card