RIVERMAX = 7
DECKLENGTH = 52

def findProb(nums, numSet, ranks):
    if "threeKind" in ranks:
        return 1
    elif "pair" not in ranks and len(nums) == 6:
        return 0
    else: 
        total = 0
        for card in numSet:
            total += calculate(nums, nums.count(card))
        return total


def calculate(cards, count):
    cards_to_be_flipped = RIVERMAX - len(cards)
    #total = math.comb(len(numSet), 1) this is calculating all at once, only want one at a time
    total = 1
    if count == 1 and len(cards) != 6:
        for i in range(cards_to_be_flipped):
            total *= (3 - i)/(DECKLENGTH - len(cards) - i)
    elif count == 1 and len(cards) == 6:
        return 0
    elif count == 2:
        total = (2 * cards_to_be_flipped)/(DECKLENGTH - len(cards))
    return total

    '''
    could also be adding = 2/(DECKLENGTH - len(cards)) * cards_to_be_flipped, then total *= adding
    '''

    # P(three of a kind | one card) = P(one card | three of a kind) * P(three of a kind)
    #                                   -----------------------------------------------
    #                                                   P(one card)

    # P(pair | one card) = P(one card | pair) * P(pair)
    #                       ---------------------------
    #                               P(one card)

    '''
    (6 choose 1) * 1/46
    (5 choose 1) * 1/47 + (1/47 * 1/46)

    (5 choose 1) * (1/47 * 1/46)

            (5)
            (1)                          1
            ----            *           ---
    len(deck) - len(cards)    len(deck) - len(cards) - 1

    RIVERMAX = 7


    total = binom(len(cards), 1)
    for i in range(RIVERMAX - len(cards)):
        total /= (len(deck) - len(cards) - i)

    '''
nums = [1, 4, 5, 2, 6]
numSet = set(nums)
ranks = ["pair"]
print(findProb(nums, numSet, ranks))
