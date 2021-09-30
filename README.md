# poker-takehome
Swept coding challenge allowing you to showcase your logic handling and code structuring abilities. 

## Overview
Write a simple app that can take two 5-card poker hands, classify each hand, and determine which hand would win. For this problem suits are ignored, __so a flush will not be possible__.

Each card can be represented by a single character:
- `A` for ace
- `K` for king
- `Q` for queen
- `J` for jack
- `T` for ten
- `2-9` for the remaining
- `*` for a wild card (max of 1 per hand)

## Hand Classifications
Hand classifications are as follows (highest to lowest):
- four-of-a-kind (4 cards of the same value: `AAAA5`)
- full house (3 of one, and 2 of another: `KKKQQ`)
- straight (all 5 in sequential order: `6789T`)
- three-of-a-kind (3 cards of the same value: `KKK23`)
- two pair (`AA33J`)
- pair (`44KQA`)
- high card (nothing else: `A267J`)

## Comparison Rules
When comparing two pair hands, compare the highest pair first, then the next pair (i.e. `AA223 > KKQQT`, since `AA > KK`). When the highest pair is a tie, move on to the next pair (i.e. `AA993 > AA88K`).

Similarly, when comparing full house hands, the three-card group is compared first (i.e. `AAA22 > KKKQQ`).

In the case of ties, determine a winner by comparing the next highest card in the hand (i.e. `AA234 < AA235` because `AA`s tie, `2`s tie, `3`s tie, but `4 < 5`).

Straights are compared by the highest card in the hand, _except_ for `A2345`, in which case the 5 is considered the highest card in the straight.

## Wild Cards
When there is a wild card (`*`), the final hand has to be a valid 5-card poker hand (__no five-of-a-kind!__)

## Results
For each comparison, display the classification and indicate which hand would win or that the result is a tie.

Examples:
- `AAAKT` vs `22233`: AAAKT three-of-a-kind < 22233 full house
- `2345*` vs `KKJJ2`: 2345* straight > KKJJ2 two pair
- `AAKKT` vs `AAKKT`: AAKKT two pair == AAKKT two pair
- `KKKKA` vs `KKKK*`: KKKKA four-of-a-kind == KKKK* four-of-a-kind

## Evaluation Criteria
Don't worry about the visuals. Plain text inputs are totally fine. We're just looking for clean code.

1. Ease of understanding code structure and logic
2. Ease of running module and testing specific hands
3. Proper handling of inputs, edge cases and wild cards
4. Well documented README.md
5. Bonus points for including some unit Tests for core logic

## Steps you should take
1. Go through the requirements and let us know if you have any questions
2. Come up with a realistic estimate of how long it will take you to get this done
3. Share your GitHub repo for the take-home with us