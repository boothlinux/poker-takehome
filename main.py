from functions import get_hands_of_cards, is_four_of_a_kind, is_full_house, is_straight, is_three_of_a_kind, is_two_pair, is_pair, find_high_card, compare_hands

def main():
    choice = input("Enter 'E' without quotes to input your own hand,\nor any other key to auto-play the game \n")

    if 'E' in choice:
        hand1 = input("Enter 5 cards for the first hand seperated by a space\n")
        hand2 = input("Enter 5 cards for the second hand seperated by a space\n")
        print(f'You chose {hand1} as your first hand and {hand2} and your second hand\n')

        #Make these into lists, converting all letters to uppercase as well
        hand1 = hand1.split(" ")
        for i in range(len(hand1)):
            hand1[i] = hand1[i].upper()
        hand2 = hand2.split(" ")
        for i in range(len(hand2)):
            hand2[i] = hand2[i].upper()


        compare_hands([hand1, hand2])
    else:
        compare_hands(get_hands_of_cards(2,5))

if __name__ == "__main__":
    main()



