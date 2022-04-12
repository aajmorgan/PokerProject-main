import deck_of_cards


def findProb(cards, ranks):
    if "pair" in ranks:
        return 1
    if len(cards) == 6:
        prob = 6 / 46 #### dont hard code this, leave it as its equation
                    # looks more like (6 choose 1) * 1/46
        return prob
    else:
        return 0
    # elif len(cards) == 5:
    #    probCurrentGetsPair =
    #   probGetPairFromLastTwo =
    #  prob = probCurrentGetsPair + probGetPairFromLastTwo
