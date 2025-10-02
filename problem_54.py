"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
Consider the following five hands dealt to two players:

Hand Player 1 Player 2 Winner
1 5H 5C 6S 7S KD Pair of Fives 2C 3S 8S 8D TD Pair of Eights Player 2
2 5D 8C 9S JS AC Highest card Ace 2C 5C 7D 8S QH Highest card Queen Player 1
3 2D 9C AS AH AC Three Aces 3D 6D 7D TD QD Flush  with Diamonds Player 2
4 4D 6S 9H QH QC Pair of Queens Highest card Nine 3D 6D 7H QD QS Pair of Queens Highest card Seven Player 1
5 2H 2D 4C 4D 4S Full House With Three Fours 3C 3D 3S 9S 9D Full House with Three Threes Player 1

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
How many hands does Player 1 win?
"""
def read_file():
    player_1 = {}
    player_2 = {}
    with open('poker.txt') as file:
        i = 1
        for line in file:
            hands = line.split()
            player_1[i] = hands[0:5]
            player_2[i] = hands[5:]
            i += 1
    return player_1, player_2

def  determine_hand(hand: list):
    def letter_for_number(hand: [str]) -> [int]:
        return  sorted([int(x[0].replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for x in hand])

    def is_flush(hand: list) -> bool:
        hand_length = len(hand)
        # Check suits 
        suits = [x[1] for x in hand if x[1] == hand[0][1]]

        if len(suits) == hand_length:
            return True
        return False
    
    def is_straight(hand: list) -> int or bool:
        high = letter_for_number(hand)
        low = letter_for_number(hand)

        high_straight = (high == list(range(min(low), max(high) + 1)))
        low_straight = (low == list(range(min(low), max(low) + 1)))

        if high_straight:
            return max(high)
        elif low_straight:
            return max(low)
        else:
            return False

    def is_royal_flush(hand: list) -> bool:
        face_cards = [x[0] for x in hand if x[0] in 'TJQKA']
        if is_flush(hand) and len(face_cards) == len(hand):
            return True

        return False

    def is_straight_flush(hand: list) -> int or bool:
        if is_flush(hand) and is_straight(hand):
            return is_straight(hand)

        return False
       
    def is_four_of_a_kind(hand: list) -> (int, int) or bool:
        control = [str(x) for x in range(2, 15)]
        face_cards = letter_for_number(hand)
        for card in control:
            if card in face_cards:
                total = face_cards.count(card)
                if total == 4:
                    return int(card), int([x for x in face_cards if x != card][0])
        return False

    def is_three_of_a_kind(hand: list) -> (int, int, int) or bool:
        control = [str(x) for x in range(2, 15)]
        face_cards = [str(x) for x in letter_for_number(hand)]
        for card in control:
            if card in face_cards:
                total = face_cards.count(card)
                if total == 3:
                    return int(card), sorted([int(x) for x in face_cards if x != card], reverse=True)
        return False

    def is_two_pair(hand: list) -> (int, int, int, int) or bool:
        pairs = []
        control = [str(x) for x in range(2, 15)]
        face_cards = [str(x) for x in letter_for_number(hand)]
        for card in control:
            if card in face_cards:
                total = face_cards.count(card)
                if total == 2:
                    pairs.append(card)
        if len(pairs) == 2:
            return sorted(pairs, reverse=True), [int(x) for x in face_cards if x not in pairs][0]
        return False

    def is_one_pair(hand: list) -> (int, int, int, int) or bool:
        control = [str(x) for x in range(2, 15)]
        face_cards = [x[0].replace('T', '10').replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in hand]
        for card in control:
            if card in face_cards:
                total = face_cards.count(card)
                if total == 2:
                    return int(card), sorted([int(x) for x in face_cards if x != card], reverse=True)
        return False

    def is_full_house(hand: list) -> (int, int) or bool:
        if is_three_of_a_kind(hand) and is_one_pair(hand):
            trips = is_three_of_a_kind(hand)[0]
            pair = is_one_pair(hand)[0]
            return trips, pair
        return False


    if is_royal_flush(hand):
        return (10)
    elif is_straight_flush(hand):
        return (9, is_straight_flush(hand))
    elif is_four_of_a_kind(hand):
        first, second = is_four_of_a_kind(hand)
        return (8, first, second)
    elif is_full_house(hand):
        trips, pair = is_full_house(hand)
        return (7, trips, pair)
    elif is_flush(hand):
        one, two, three, four, five = sorted(letter_for_number(hand), reverse=True)
        return (6, one, two, three, four, five)
    elif is_straight(hand):
        return (5, is_straight(hand))
    elif is_three_of_a_kind(hand):
        card, [one, two] = is_three_of_a_kind(hand)
        return (4, card, one, two)
    elif is_two_pair(hand):
        [pair_one, pair_two], remainder = is_two_pair(hand)
        return (3, pair_one, pair_two, remainder)
    elif is_one_pair(hand):
        pair, [one, two, three] = is_one_pair(hand)
        return (2,  pair, one, two, three)
    else:
        one, two, three, four, five = sorted(letter_for_number(hand), reverse=True)
        return (1, one, two, three, four, five)

    
def check_hands(player_1: dict, player_2: dict) -> int:
    player_1_wins = 0
    player_2_wins = 0
    for hand in range(1, 1001):
        player_1_hand =  determine_hand(player_1[hand])
        player_2_hand =  determine_hand(player_2[hand])

        count = max([len(player_1_hand), len(player_2_hand)])

        for i in range(0, count+1):
            if player_1_hand[i] > player_2_hand[i]:
                player_1_wins += 1
                break
            elif player_2_hand[i] > player_1_hand[i]:
                player_2_wins += 1
                break
          

    
    return player_1_wins, player_2_wins


if __name__ == '__main__':
    player_1, player_2 = read_file()

    player_1_wins, player_2_wins = check_hands(player_1, player_2)
    print(f"Player One Wins: {player_1_wins}\nPlayer Two Wins: {player_2_wins}")