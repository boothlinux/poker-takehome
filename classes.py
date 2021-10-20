class PlayingCard:
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

    def __init__(self, value=0, suit=0):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return (self.value)