import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

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
                
    def __str__(self):
    	deck_comp = ''
    	for card in self.deck:
    		deck_comp += '\n' + card.__str__()
    	return "The deck has: " + deck_comp

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()   


class Hand:
    
    def __init__(self):
    	# A new hand has no cards
    	self.cards = [] 
    	self.total_value = 0
    	self.aces = 0

    #def __str__(self):  
    #	return 'Cards: ' + ', '.join([str(card.value) for card in self.cards])

    def __str__(self):  
    	str_cards = ''
    	for card in self.cards:
    		str_cards += '\n' + card.__str__()
    	return "Cards: " + str_cards

    def add_card(self,card):
    	# Card passed in from Deck.deal()
    	self.cards.append(card)
    	self.total_value += card.value
    	if card.rank == 'Ace':
    		self.aces += 1

    def adjust_for_ace(self):
    	# If total_value > 21 and self.aces > 0 then change my ace to be a 1 instead of an 11
    	while self.total_value > 21 and self.aces > 0:
    		self.total_value -= 10
    		self.aces -= 1


class Chips:
	
	def __init__(self,amount=100):
		self.amount = amount
		self.bet = 0

	def __str__(self):
		return("Player has {} chips".format(self.amount))

	def win_bet(self):
		self.amount += self.bet
		self.bet = 0

	def lose_bet(self):
		self.amount -= self.bet
		self.bet = 0



def hit_or_stand():
    player_decision = ''
    while not (player_decision == 'H' or player_decision == 'S'):
        print("")
        player_decision = input('Hit (h/H) or Stand (s/S) ?: ').upper()
    return player_decision


def take_bet():
	while True:
		try:
			print("")
			player_chips.bet = int(input('How many chips would you like to bet (1-{})?: '.format(player_chips.amount)))
		except ValueError:
			print('Sorry, a bet must be an integer')
		else:
			if player_chips.bet > player_chips.amount:
				print("Sorry, your bet can't exceed {}".format(player_chips.amount))
			elif player_chips.bet <= 0:
				print("Sorry, your bet needs to be higher than 0")
			else:
				break

def play_again():
    player_decision = ''
    while not (player_decision == 'Y' or player_decision == 'N'):
        print("")
        player_decision = input('Do you want to play again (y/Y or n/N) ?: ').upper()
    if player_decision == 'Y':
    	return True
    else:
    	return False


print("")
print("####################")
print("#  BLACKJACK GAME  #")
print("####################")
print("")

new_deck = Deck()
print("Shuffling the deck...")
new_deck.shuffle()

player_chips = Chips()
print("")
print(player_chips)

game_on = True

while game_on == True:
	take_bet()
	
	print("")
	print("Dealing first two cards to the Player...")
	player_hand = Hand()
	player_hand.add_card(new_deck.deal_one())
	player_hand.adjust_for_ace()
	player_hand.add_card(new_deck.deal_one())
	player_hand.adjust_for_ace()
	print(player_hand)
	
	print("")
	print("Dealing first two cards to the Dealer...")
	dealer_hand = Hand()
	dealer_hand.add_card(new_deck.deal_one())
	dealer_hand.adjust_for_ace()
	dealer_hand.add_card(new_deck.deal_one())
	dealer_hand.adjust_for_ace()
	print("Cards:")
	print(str(dealer_hand.cards[0].__str__()))
	print("<card_hidden>")

	#################
	# PLAYER's TURN #
	#################
	print("")
	print("##########")
	print("# PLAYER #")
	print("##########")
	
	player_game_on = True
	
	while player_game_on == True:
		print(player_hand)
		player_decision = hit_or_stand()
		if player_decision == "H":
			card = new_deck.deal_one()
			player_hand.add_card(card)
			player_hand.adjust_for_ace()

			if player_hand.total_value > 21:
				print(player_hand)
				print("")
				print("PLAYER: {}".format(player_hand.total_value))
				print("DEALER WON !!")
				player_chips.lose_bet()
				player_game_on = False
				if player_chips.amount > 0:
					game_on = play_again()
				else:
					print("Sorry, you run out of chips")
					game_on = False
			elif player_hand.total_value == 21:
				print(player_hand)
				print(player_hand.total_value)
				print("")
				print("PLAYER: {}".format(player_hand.total_value))
				print("PLAYER WON !!")
				player_chips.win_bet()
				player_game_on = False
				game_on = play_again()
			else:
				player_game_on = True
		else:
			player_game_on = False
			
			#################
			# DEALER's TURN #
			#################
	
			print("")
			print("##########")
			print("# DEALER #")
			print("##########")
	
			dealer_game_on = True
			
			while dealer_game_on == True:
				if dealer_hand.total_value > 21:
					print(dealer_hand)
					print("")
					print("PLAYER: {}".format(player_hand.total_value))
					print("DEALER: {}".format(dealer_hand.total_value))
					print("PLAYER WON !!")
					player_chips.win_bet()
					dealer_game_on = False
					game_on = play_again()
				elif dealer_hand.total_value <= player_hand.total_value:
					dealer_game_on = True
					card = new_deck.deal_one()
					dealer_hand.add_card(card)
					dealer_hand.adjust_for_ace()
				else:
					print(dealer_hand)
					print("")
					print("PLAYER: {}".format(player_hand.total_value))
					print("DEALER: {}".format(dealer_hand.total_value))
					print("DEALER WON !!")
					player_chips.lose_bet()
					dealer_game_on = False
					if player_chips.amount > 0:
						game_on = play_again()
					else:
						print("Sorry, you run out of chips")
						game_on = False
	
			
			
			
			
			