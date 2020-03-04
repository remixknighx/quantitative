# -*- coding: utf-8 -*-
"""
1309. Decrypt String from Alphabet to Integer Mapping
@link https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha_int_dict = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i', '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u', '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        s_reverse = s[::-1]
        count = 0
        result = ''
        while True:
            if s_reverse[count] == '#':
                result += alpha_int_dict[s_reverse[count: count + 3][::-1]]
                count += 3
            else:
                result += alpha_int_dict[s_reverse[count]]
                count += 1

            if count == len(s_reverse):
                break

        return result[::-1]


if __name__ == '__main__':
    print(Solution().freqAlphabets(s="10#11#12"))
    print(Solution().freqAlphabets(s="1326#"))
    print(Solution().freqAlphabets(s="25#"))
    print(Solution().freqAlphabets(s="12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))
