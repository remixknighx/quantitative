# -*- coding: utf-8 -*-
"""
36. Valid Sudoku
@link https://leetcode.com/problems/valid-sudoku/
"""
from typing import List
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_result = self.checkRowAndColumn(row)
            if row_result is False:
                return False

        for j in range(0, 9):
            column = []
            for i in range(0, 9):
                column.append(board[i][j])
            col_result = self.checkRowAndColumn(column)
            if col_result is False:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                box.extend([board[i][j], board[i][j + 1], board[i][j + 2], board[i + 1][j], board[i + 1][j + 1],
                            board[i + 1][j + 2], board[i + 2][j], board[i + 2][j + 1], board[i + 2][j + 2]])
                box_result = self.checkRowAndColumn(box)
                if box_result is False:
                    return False

        return True


    def checkRowAndColumn(self, num_list: List[str]):
        row_count = Counter(num_list)
        for (k, v) in row_count.items():
            if k != '.' and v > 1:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(
        board=[[".", ".", ".", ".", "5", ".", ".", "1", "."],
               [".", "4", ".", "3", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "3", ".", ".", "1"],
               ["8", ".", ".", ".", ".", ".", ".", "2", "."],
               [".", ".", "2", ".", "7", ".", ".", ".", "."],
               [".", "1", "5", ".", ".", ".", ".", ".", "."],
               [".", ".", ".", ".", ".", "2", ".", ".", "."],
               [".", "2", ".", "9", ".", ".", ".", ".", "."],
               [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
