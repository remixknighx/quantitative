# -*- coding: utf-8 -*-
"""
1275. Find Winner on a Tic Tac Toe Game
@link https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
"""
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['' for x in range(3)] for y in range(3)]
        for r in range(len(moves)):
            rowPos = moves[r][0]
            colPos = moves[r][1]
            character = 'A' if r % 2 == 0 else 'B'
            board[rowPos][colPos] = character
            if self.checkWinner(board, rowPos, colPos, character):
                return character

        return 'Draw' if len(moves) == 9 else 'Pending'

    def checkWinner(self, board: List[List[str]], row: int, col: int, c: str) -> bool:
        # horizontal check
        if c == board[row][0] and c == board[row][1] and c == board[row][2]:
            return True

        # vertical check
        if c == board[0][col] and c == board[1][col] and c == board[2][col]:
            return True

        # diagonal left check
        if c == board[0][0] and c == board[1][1] and c == board[2][2]:
            return True

        # diagonal right check
        if c == board[0][2] and c == board[1][1] and c == board[2][0]:
            return True

        return False


if __name__ == '__main__':
    print(Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]))
