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
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below).

But if two ranks tie, for example, both players have a pair of queens,
then highest cards in each hand are compared (see example 4 below);

if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	    Winner
1	 	5H 5C 6S 7S KD      2C 3S 8S 8D TD   	Player 2
        Pair of Fives       Pair of Eights

2	 	5D 8C 9S JS AC      2C 5C 7D 8S QH      Player 1
        Highest card Ace    Highest card Queen

3	 	2D 9C AS AH AC      3D 6D 7D TD QD      Player 2
        Three Aces          Flush with Diamonds

4	 	4D 6S 9H QH QC      3D 6D 7H QD QS      Player 1
        Pair of Queens      Pair Queens
        Highest card Nine   High card 7

5	 	2H 2D 4C 4D 4S      3C 3D 3S 9S 9D      Player 1
        Full House          Full House
        With Three Fours    With Three Threes

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space):
the first five are Player 1's cards and the last five are Player 2's cards.

You can assume that all hands are valid (no invalid characters or repeated cards),
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""

# T = 10, J = 11, Q = 12, K = 13, A = 14
def sort_hand(hand):
    v = [h[0] for h in hand]
    suits = [h[1] for h in hand]
    for i in range(0,5):
        if v[i] == 'T': v[i] = '10'
        if v[i] == 'J': v[i] = '11'
        if v[i] == 'Q': v[i] = '12'
        if v[i] == 'K': v[i] = '13'
        if v[i] == 'A': v[i] = '14'
    new_hand = []
    for i in range(0,5):
        new_hand.append([int(v[i]), suits[i]])
    new_hand.sort()
    return new_hand

def rank_hand(hand):
    vals = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    different_cards = len(set(vals))
    same_suit = len(set(suits)) == 1
    consecutive = [*range(vals[0],vals[0]+5)] == vals
    if consecutive and same_suit:
        if vals == [*range(10,15)]:
            return 'royal flush'
        else:
            return 'straight flush'
    if different_cards == 2:
        if sum([v == vals[0] for v in vals]) == 4 or sum([v == vals[-1] for v in vals]) == 4:
            return 'four kind'
        return 'full house'
    if same_suit:
        return 'flush'
    if consecutive:
        return 'straight'
    if different_cards == 3:
        if sum([v == vals[0] for v in vals]) == 3 or sum([v == vals[1] for v in vals]) == 3 or sum([v == vals[2] for v in vals]) == 3:
            return 'three kind'
        return 'two pair'
    if different_cards == 4:
        return 'one pair'
    return 'high card'

def resolve_tie(h1, h2, rank):
    # not considering ties: "in each hand there is a clear winner"
    v1 = [c[0] for c in h1]
    v2 = [c[0] for c in h2]

    if rank == 'straight flush':    # tie breaker is high card
        return 1 if v1[-1] > v2[-1] else 2

    if rank == 'four kind':         # tie breaker is highest four of a kind
        h1_four_kind = v1[0] if sum([v == v1[0] for v in v1]) == 4 else v1[-1]
        h2_four_kind = v2[0] if sum([v == v2[0] for v in v2]) == 4 else v2[-1]
        return 1 if h1_four_kind > h2_four_kind else 2

    if rank == 'full house' or rank == 'three kind':        # tie breaker is highest three of a kind
        if sum([v == v1[0] for v in v1]) == 3:
            h1_three_kind = v1[0]
        if sum([v == v1[1] for v in v1]) == 3:
            h1_three_kind = v1[1]
        h1_three_kind = v1[2]

        if sum([v == v2[0] for v in v2]) == 3:
            h2_three_kind = v2[0]
        if sum([v == v2[1] for v in v2]) == 3:
            h2_three_kind = v2[1]
        h2_three_kind = v2[2]
        return 1 if h1_three_kind > h2_three_kind else 2

    if rank == 'two pair':
        h1_pairs = []
        h2_pairs = []
        for i in range(4):
            if v1[i] == v1[i+1]:
                h1_pairs.append(v1[i])
            if v2[i] == v2[i+1]:
                h2_pairs.append(v2[i])

        if h1_pairs[-1] == h2_pairs[-1]:
            if h1_pairs[0] == h2_pairs[0]:
                h1_single = list(filter(lambda x: x not in h1_pairs, v1))
                h2_single = list(filter(lambda x: x not in h2_pairs, v2))
                return 1 if h1_single > h2_single else 2

    if rank == 'one pair':
        for i in range(4):
            if v1[i] == v1[i + 1]:
                h1_pair = v1[i]
            if v2[i] == v2[i + 1]:
                h2_pair = v2[i]
        if h1_pair == h2_pair:
            h1_singles = list(filter(lambda x: x != h1_pair, v1))
            h2_singles = list(filter(lambda x: x != h2_pair, v2))
            for i in range(2, -1, -1):
                if h1_singles[i] != h2_singles[i]:
                    return 1 if h1_singles[i] > h2_singles[i] else 2
        return 1 if h1_pair > h2_pair else 2

    if rank=='high card':
        for i in range(4, -1, -1):
            if v1[i] != v2[i]:
                return 1 if v1[i] > v2[i] else 2

def winner(p1, p2):
    ranks = ['high card', 'one pair', 'two pair', 'three kind', 'straight', 'flush', 'full house', 'four kind', 'straight flush', 'royal flush']
    hand1 = sort_hand(p1)
    hand2 = sort_hand(p2)
    r1 = ranks.index(rank_hand(hand1))
    r2 = ranks.index(rank_hand(hand2))
    if r1 == r2:
        return resolve_tie(hand1, hand2, ranks[r1])
    return 1 if r1 > r2 else 2

def total_player_one():
    f = open("../resources/p054_poker.txt", "r")
    all_cards = f.read().splitlines()
    f.close()
    p1_wins = 0
    for c in all_cards:
        cards = c.split()
        p1 = cards[:5]
        p2 = cards[5:]
        if winner(p1, p2) == 1:
            p1_wins += 1
    return p1_wins

# test
print(sort_hand(['KD', '5C', '6S', '5H', '7S'])==[[5,'C'], [5,'H'], [6,'S'], [7,'S'], [13, 'D']])

print(rank_hand([[10,'D'],[11,'D'],[12,'D'],[13,'D'],[14,'D']])=='royal flush')
print(rank_hand([[9,'D'],[10,'D'],[11,'D'],[12,'D'],[13,'D']])=='straight flush')
print(rank_hand([[9,'D'],[9,'H'],[9,'S'],[9,'C'],[13,'D']])=='four kind')
print(rank_hand([[9,'D'],[13,'D'],[13,'H'],[13,'S'],[13,'C']])=='four kind')
print(rank_hand([[9,'D'],[9,'H'],[9,'S'],[13,'D'],[13,'C']])=='full house')
print(rank_hand([[9,'D'],[9,'H'],[13,'S'],[13,'D'],[13,'C']])=='full house')
print(rank_hand([[2,'D'],[4,'D'],[6,'D'],[8,'D'],[13,'D']])=='flush')
print(rank_hand([[9,'D'],[10,'D'],[11,'D'],[12,'D'],[13,'H']])=='straight')
print(rank_hand([[9,'D'],[10,'D'],[13,'S'],[13,'D'],[13,'H']])=='three kind')
print(rank_hand([[9,'D'],[9,'H'],[9,'S'],[13,'D'],[14,'H']])=='three kind')
print(rank_hand([[2,'D'],[9,'H'],[9,'S'],[9,'D'],[13,'H']])=='three kind')
print(rank_hand([[2,'D'],[2,'H'],[3,'S'],[13,'D'],[13,'H']])=='two pair')
print(rank_hand([[2,'D'],[3,'H'],[3,'S'],[13,'D'],[13,'H']])=='two pair')
print(rank_hand([[2,'D'],[2,'H'],[3,'S'],[3,'D'],[13,'H']])=='two pair')
print(rank_hand([[2,'D'],[2,'H'],[3,'S'],[4,'D'],[13,'H']])=='one pair')
print(rank_hand([[2,'D'],[3,'H'],[3,'S'],[4,'D'],[13,'H']])=='one pair')
print(rank_hand([[2,'D'],[3,'H'],[4,'S'],[4,'D'],[13,'H']])=='one pair')
print(rank_hand([[2,'D'],[3,'H'],[5,'S'],[13,'D'],[13,'H']])=='one pair')
print(rank_hand([[2,'D'],[3,'H'],[5,'S'],[13,'D'],[14,'H']])=='high card')

print(resolve_tie([[9,'D'],[10,'D'],[11,'D'],[12,'D'],[13,'D']], [[2,'D'],[3,'D'],[4,'D'],[5,'D'],[6,'D']], 'straight flush')==1)
print(resolve_tie([[3,'D'],[3,'H'],[3,'S'],[3,'C'],[13,'D']], [[2,'D'],[6,'C'],[6,'H'],[6,'S'],[6,'D']], 'four kind')==2)
print(resolve_tie([[9,'D'],[9,'H'],[9,'S'],[13,'D'],[13,'C']], [[8,'D'],[8,'H'],[8,'S'],[13,'S'],[13,'H']], 'full house')==1)
print(resolve_tie([[2,'D'],[9,'H'],[9,'S'],[9,'D'],[10,'C']], [[8,'D'],[8,'H'],[8,'S'],[12,'S'],[14,'H']], 'three kind')==1)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[3,'D'],[13,'H']], [[4,'D'],[4,'H'],[9,'S'],[13,'D'],[13,'H']], 'two pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[13,'C'],[13,'S']], [[4,'D'],[4,'H'],[9,'S'],[13,'D'],[13,'H']], 'two pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[13,'C'],[13,'S']], [[2,'D'],[2,'H'],[9,'S'],[13,'D'],[13,'H']], 'two pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[4,'C'],[13,'S']], [[2,'D'],[3,'H'],[9,'S'],[13,'D'],[13,'H']], 'one pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[4,'C'],[10,'S']], [[2,'D'],[2,'H'],[9,'S'],[11,'D'],[13,'H']], 'one pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[4,'C'],[13,'S']], [[2,'D'],[2,'H'],[9,'S'],[11,'D'],[13,'H']], 'one pair')==2)
print(resolve_tie([[2,'D'],[2,'H'],[3,'S'],[11,'C'],[13,'S']], [[2,'D'],[2,'H'],[9,'S'],[11,'D'],[13,'H']], 'one pair')==2)
print(resolve_tie([[2,'D'],[3,'H'],[5,'S'],[11,'C'],[13,'S']], [[2,'D'],[6,'H'],[7,'S'],[8,'D'],[14,'H']], 'high card')==2)

p1=['5H', '5C', '6S', '7S', 'KD']
p2=['2C', '3S', '8S', '8D', 'TD']
print(winner(p1, p2)==2)

# solution
print(total_player_one())