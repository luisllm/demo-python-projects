import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()   



class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        # Note we remove one card from the list of all_cards
        # We state 0 to remove from the "top" of the deck
        # We'll imagine index -1 as the bottom of the deck
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'





new_deck = Deck()
#print(len(new_deck.all_cards))
#print(new_deck.all_cards[0])
print("Shuffling the deck...")
new_deck.shuffle()

player1 = Player("One")
player2 = Player("Two")
print("")
print("Dealing...")
for x in range(26):
	player1.add_cards(new_deck.deal_one())
	player2.add_cards(new_deck.deal_one())

print("")
print(player1)
print(player2)
print("")
print("The game is about to start...")

game_on = True
war_tie = False
round_num = 0

while game_on == True:
	round_num += 1
	print("")
	print("Round: {}".format(round_num))
	print(player1)
	print(player2)

	#################################
	# Check if the game is finished #
	#################################
	# If war_tie is False then all you need is at least 1 card.
	# If war_tie is True, then you need at least 3 cards

	if (war_tie == False and len(player1.all_cards) == 0) or (war_tie == True and len(player1.all_cards) < 3):
		print("PLAYER2 WON !!")
		game_on = False
		break
	
	if (war_tie == False and len(player2.all_cards) == 0) or (war_tie == True and len(player2.all_cards) < 3):
		print("PLAYER1 WON !!")
		game_on = False
		break

	#####################
	# Start a new round #
	#####################

	# If war_tie is False, we need to start with no cards on the table
	if war_tie == False:
		table_cards = []

		player1_table_card = player1.remove_one()
		player2_table_card = player2.remove_one()
		print("")
		print("Player1's card: {}".format(player1_table_card))
		print("Player2's card: {}".format(player2_table_card))

		table_cards.append(player1_table_card)
		table_cards.append(player2_table_card)
	# If it was a war (tie), each player has to play 3 additional cards on the table
	else:
		# 3 cards from player1
		table_cards.append(player1.remove_one())
		table_cards.append(player1.remove_one())
		player1_table_card = player1.remove_one()
		table_cards.append(player1_table_card)

		# 3 cards from player2
		table_cards.append(player2.remove_one())
		table_cards.append(player2.remove_one())
		player2_table_card = player2.remove_one()
		table_cards.append(player2_table_card)
		
		print("")
		print("Player1's card: {}".format(player1_table_card))
		print("Player2's card: {}".format(player2_table_card))



	if player1_table_card.value > player2_table_card.value:
		print("Player1's card is higher")
		player1.add_cards(table_cards)
		war_tie = False
	elif player1_table_card.value < player2_table_card.value:
		print("Player2's card is higher")
		player2.add_cards(table_cards)
		war_tie = False
	else:
		print("It is a war tie")
		war_tie = True
		continue



