# -*- coding: utf-8 -*-
"""
79. Word Search
@link https://leetcode.com/problems/word-search/
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == [[]]:
            return False

        self.used = {}
        self.i = 0

        def check(x, y):
            if board[y][x] != word[self.i]:
                return False

            # make sure we have not used before
            key = (x, y)
            if key in self.used:
                return False
            self.used[key] = 1
            self.i += 1

            # if length matches we are done!
            if self.i == len(word):
                return True
            # try going right
            if x + 1 < len(board[0]) and check(x + 1, y):
                return True
            # try going down
            if y + 1 < len(board) and check(x, y + 1):
                return True
                # try going up
            if y - 1 >= 0 and check(x, y - 1):
                return True
            # try going left
            if x - 1 >= 0 and check(x - 1, y):
                return True
            self.i -= 1
            del self.used[key]  # step back

            return False

        for y in range(len(board)):
            for x in range(len(board[0])):
                if check(x, y):
                    return True
        return False


if __name__ == '__main__':
    board = [['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    print(Solution().exist(board=board, word=word))