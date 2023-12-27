import collections

# Named tuple to represent a playing card
Card = collections.namedtuple('Card', ['rank', 'suit'])

def create_deck():
	# Use letters to represent suits: 'S' for Spades, 'H' for Hearts, 'D' for Diamonds, 'C' for Clubs
	suits = 'SHDC'
	ranks = '23456789TJQKA'

	# Create the deck with all possible combinations of ranks and suits
	cards = [
		Card(rank, suit)
		for suit in suits
		for rank in ranks
		]

	# List to track dealt cards
	dealt_cards = []
	# Note: we need two returned items
	return cards, dealt_cards

def deal_card(deck):
	# Deal a card from the top of the deck
	dealt_card = deck[0].pop()
	# Track the dealt card
	deck[1].append(dealt_card)
	# Note: we need two returned items
	return dealt_card, deck

# Example usage:
deck = create_deck()
print(f"Initial deck: {deck[0]}")

# Deal the first card and display the updated deck
dealt_card1, deck = deal_card(deck)
print(f"Dealt card 1: {dealt_card1}")
print(f"Updated deck: {deck[0]}")
print(f"Dealt cards: {deck[1]}") # Display the list of dealt cards

# Deal another card and display the updated deck
dealt_card2, deck = deal_card(deck)
print(f"Dealt card 2: {dealt_card2}")
print(f"Updated deck: {deck[0]}")
print(f"Dealt cards: {deck[1]}") # Display the list of dealt cards
