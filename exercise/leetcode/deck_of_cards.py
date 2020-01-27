# -*- coding: utf-8 -*-
"""
914. X of a Kind in a Deck of Cards
@link https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
"""
from typing import List
from collections import Counter
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            # Quick response:
            # if deck size < 2 (i.e., lower bound of partition size)
            return False

        card_occ_dict = Counter(deck)

        if len(card_occ_dict) == 1:
            # Quick response:
            # if deck consists of only one number
            return True

        highest_common_factor = card_occ_dict[deck[0]]
        for card, occ in card_occ_dict.items():

            # The highest common factor of occurrence must be >= 2 to make a successful partition
            highest_common_factor = gcd(highest_common_factor, occ)

            if highest_common_factor == 1:
                return False

        return True


if __name__ == '__main__':
    deck = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    print(Solution().hasGroupsSizeX(deck=deck))
