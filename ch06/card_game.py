# ccc99s1 - card game
# https://dmoj.ca/problem/ccc99s1
HIGH_CARDS = ['jack', 'queen', 'king', 'ace']
CARDS_NAMES = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
CARDS_COUNT = 52
cards = []


def contains_high_card(card_list, start_index, end_index):
    for j in range(start_index, end_index + 1):
        if card_list[j] in HIGH_CARDS:
            return True
    return False


def process_score(card_list, index):
    if card_list[index] == 'jack' \
            and index + 1 < CARDS_COUNT \
            and contains_high_card(card_list, start_index=index + 1, end_index=index + 1):
        return 1
    elif card_list[index] == 'queen' \
            and index + 2 < CARDS_COUNT \
            and not contains_high_card(card_list, start_index=index + 1, end_index=index + 2):
        return 2
    elif card_list[index] == 'king' \
            and index + 3 < CARDS_COUNT \
            and not contains_high_card(card_list, start_index=index + 1, end_index=index + 3):
        return 3
    elif card_list[index] == 'ace' \
            and index + 4 < CARDS_COUNT \
            and not contains_high_card(card_list, start_index=index + 1, end_index=index + 4):
        return 4
    else:  # not (card_list[index] in HIGH_CARDS) or (not index in range)
        return 0


for i in range(CARDS_COUNT):
    card = input()
    if not (card in CARDS_NAMES):
        exit(f"not {card} in CARDS_NAMES")
    cards.append(card)
aScore = 0
aTotalScore = 0
bScore = 0
bTotalScore = 0
for i in range(CARDS_COUNT):
    if i % 2 == 0:
        aScore = process_score(cards, i)
        if aScore > 0:
            print(f"Player A scores {aScore} point(s).")
            aTotalScore += aScore
    else:  # i % 2 != 0
        bScore = process_score(cards, i)
        if bScore > 0:
            print(f"Player B scores {bScore} point(s).")
            bTotalScore += bScore
print(f"Player A: {aTotalScore} point(s).")
print(f"Player B: {bTotalScore} point(s).")
