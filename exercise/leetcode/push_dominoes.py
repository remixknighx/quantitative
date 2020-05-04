# -*- coding: utf-8 -*-
"""
838. Push Dominoes
@link https://leetcode.com/problems/push-dominoes/
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        prevR = -1
        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                if prevR == -1:
                    j = i - 1
                    while j >= 0 and dominoes[j] != 'L':
                        dominoes[j] = 'L'
                        j -= 1
                else:
                    start = prevR + 1
                    end = i - 1
                    while start < end:
                        dominoes[start] = 'R'
                        dominoes[end] = 'L'
                        start += 1
                        end -= 1
                    prevR = -1

            if dominoes[i] == 'R':
                if prevR != -1:
                    dominoes[prevR:i] = ['R'] * (i-prevR)
                prevR = i

        if prevR != -1:
            dominoes[prevR:len(dominoes)] = ['R'] * (len(dominoes) - prevR)
        return ''.join(dominoes)


if __name__ == '__main__':
    print(Solution().pushDominoes(dominoes='.L.R...LR....'))
    print(Solution().pushDominoes(dominoes='RR.L'))
