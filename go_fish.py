from random import shuffle
from collections import Counter

class GoFishGame():
    
    MAX_TURNS=10
    CARDS_PER_HAND=7
    SUITS = ["h", "d", "c", "s"]
    FACES = [str(_) for _ in range(2, 11)] + ["j", "q", "k", "a"]

    def __init__(self, players=4):
        self.players = players
        self.deck = []
        self.reset()

    def reset(self):
        self.build_deck()
        self.hands = [[] for i in range(self.players)]
        self.next_player = 0
        self.turns_taken = 0
        self.completed_sets = set()

    def play(self):
        self.reset()
        self.deal_hands()
        self.show_hands()

        while not self.is_game_over():
            self.take_player_turn()


    def build_deck(self):
        self.deck = []
        for s in GoFishGame.SUITS:
            for f in GoFishGame.FACES:
                self.deck.append(f"{s}{f}")
        shuffle(self.deck)    

    def deal_hands(self):
        for i in range(GoFishGame.CARDS_PER_HAND):
            for j in range(self.players):
                top_card = self.deck.pop(0)
                self.hands[j].append(top_card)

    def show_hands(self):
        for hand in self.hands:
            print(",".join([c for c in hand]))

    def is_game_over(self):
        if len(self.completed_sets) == 13:
            return True
        
        return self.turns_taken >= GoFishGame.MAX_TURNS
    
    def take_player_turn(self):
        #print(f"Taking next turn ({self.turns_taken}) for player {self.next_player}")
        
        my_hand = self.hands[self.next_player]
        # check my hand for sets

        faces = [card[1] for card in my_hand]
        counts = Counter(faces)

        #print(counts)

        for face in counts:
            print(f"Player {self.next_player} has {counts[face]} {face} cards")
            if counts[face] == 4:
                print(f"A set of 4 {face} was found")
        

        # do I have any cards not part of a full set?
            # if I do, ask someone for one of them
                # if they have some of the cards I asked for, 
                #   take them, 
                #   and take another turn
                # if they don't, try to draw a card
                #   if there are no cards in the draw pile, 
                #       I'm done for this turn
                #   if I draw a card that I wanted, 
                #       show it and take another turn
                #   if I draw some other card, 
                #       I'm done for this turn
            # if I am out of cards 
            #   try to draw a card
                #   if there are no cards in the draw pile, 
                #       I'm done for the game
                #   if I draw a card that I wanted, 
                #       show it and take another turn
                #   if I draw some other card, 
                #       I'm done for this turn

        # check for sets

        # update the game state to move on to the next player's turn
        self.turns_taken += 1
        self.next_player += 1
        if self.next_player == self.players:
            self.next_player = 0

        

if __name__ == "__main__":
    game = GoFishGame()
    game.play()
