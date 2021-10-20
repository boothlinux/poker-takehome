from classes import PlayingCard
import random

def get_full_shuffled_deck_of_cards():

    """
    This function returns a 52 card deck plus one wild card as a list
    """

    #Make a deck of cards list, and a copy to modify
    deck_of_cards_without_wildcard = [PlayingCard(value, suit) for value in PlayingCard.values for suit in PlayingCard.suits]
    full_deck_of_cards = deck_of_cards_without_wildcard[:]

    #Make the wildcard a special card and add one to the deck
    wildcard = PlayingCard("*", None) 
    full_deck_of_cards.insert(52, wildcard)

    #Shuffle and return your deck
    random.shuffle(full_deck_of_cards)
    return full_deck_of_cards

def get_hands_of_cards(number_of_hands, cards_per_hand):
    """
    This functions takes two integers (number of hands and cards per hand) 
    and returns a list containing the hands requested
    """
    card_hands = []
    shuffled_deck = get_full_shuffled_deck_of_cards()
    
    for hand in range(number_of_hands):
        hand = []
        for card in range(cards_per_hand):
            hand.append(shuffled_deck[card].value)
            shuffled_deck.pop(card)
            hand.sort()
        card_hands.append(hand)
    
    return card_hands

def is_four_of_a_kind(hand):
    """
    This functions takes the hand (list) and returns true if it is four of a kind
    """
    for card in hand:
        if hand.count(card) is 4:
            return True

def is_full_house(hand):
    """
    This functions takes the hand (list) and returns true if it is a full house
    """
    two_cards = False
    three_cards = False
    for card in hand:
        if hand.count(card) is 3:
            three_cards = True
        if hand.count(card) is 2:
            two_cards = True
    
    if two_cards and three_cards:
        return True

def is_straight(hand):
    """
    This functions takes the hand (list) and returns true if it is a straight
    """
    int_converted_hand = []
    for card in hand:
        if card == 'T':
            card = 10
        if card == 'J':
            card = 11
        if card == 'Q':
            card = 12
        if card == 'K':
            card = 13
        if card == 'A':
            card = 14
        if card is not '*':
            int_converted_hand.append(int(card))

    range_list=list(range(min(int_converted_hand), max(int_converted_hand)+1))
    if int_converted_hand == range_list:
        return True

def is_three_of_a_kind(hand):
    """
    This functions takes the hand (list) and returns true if it is three of a kind
    """
    two_cards = False
    three_cards = False
    for card in hand:
        if hand.count(card) is 3:
            three_cards = True
        if hand.count(card) is 2:
            two_cards = True
        
    if three_cards:
        if not two_cards:
            return True

def is_two_pair(hand):
    """
    This functions takes the hand (list) and returns true if the hand has two pair
    """
    pair_count = 0
    for card in hand:
        if hand.count(card) is 2:
            pair_count = pair_count + 1
    if pair_count == 4:
        return True


def is_pair(hand):
    """
    This functions takes the hand (list) and returns true if it has one pair
    """
    pair_count = 0
    for card in hand:
        if hand.count(card) is 2:
            pair_count =  pair_count + 1
    if pair_count == 2:
        return True

def find_high_card(hand):
    """
    This functions takes the hand (list) and returns the highest card
    """
    high_card = max(hand)
    return high_card

def compare_hands(hands):
    """
    This functions takes the hand (list), finds the score of the hand, compares the scores and tell you who won (or if it is a tie)
    """
    hand_scores = []
    for index, hand in enumerate(hands):
        print(f'Hand number {index + 1}: {hand}')
        if is_full_house(hand):
            print(f'Full House in hand number {index + 1 } \n')
            hand_scores.append(7)
            continue
        if is_four_of_a_kind(hand):
            print(f'Four of a kind in hand number {index + 1} \n')
            hand_scores.append(6)
            continue
        if is_three_of_a_kind(hand):
            print(f'Three of a kind in hand number {index + 1} \n')
            hand_scores.append(5)
            continue
        if is_straight(hand):
            print(f'Hand number {index + 1} is a straight \n')
            hand_scores.append(4)
            continue
        if is_two_pair(hand):
            print(f'Hand number {index + 1} has two pair \n')
            hand_scores.append(3)
            continue
        if is_pair(hand):
            print(f'Hand number {index + 1} has a single pair \n')
            hand_scores.append(2)
            continue
        elif find_high_card(hand):
            hand_scores.append(1)
            high_card = find_high_card(hand)
            print(f'Hand number {index + 1} has a high card of {high_card} \n')
        else:
            hand_scores.append(0)

    if len(set(hand_scores)) <= 1:
        print("Its a tie!")

    else:
        winning_hand_score = max(hand_scores)
        winning_hand_index = hand_scores.index(winning_hand_score)
        print(f'Hand number {winning_hand_index + 1} wins!')
