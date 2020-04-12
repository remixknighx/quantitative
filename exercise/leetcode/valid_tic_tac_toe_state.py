# -*- coding: utf-8 -*-
"""
794. Valid Tic-Tac-Toe State
@link https://leetcode.com/problems/valid-tic-tac-toe-state/
"""
from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        # can generalize to n x n boards
        state = "".join(board)
        nX = state.count("X")
        nO = state.count("O")

        # players take turns
        if abs(nX - nO) > 1:
            return False

        # first player is X
        if nO > nX:
            return False

        # game ends after win
        if self.player_won("X", board) and (self.player_won("O", board) or nO == nX):
            return False

        if self.player_won("O", board) and nX > nO:
            return False

        return True

    def player_won(self, player: str, board: List[str]) -> bool:
        n = len(board)

        if n * player in board:  # row
            return True

        for i in range(n):  # column
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True

        if (board[0][0] == board[1][1] == board[2][2] == player or
                board[0][2] == board[1][1] == board[2][0] == player):  # diagonals
            return True

        return False


if __name__ == '__main__':
    print(Solution().validTicTacToe(board=["O  ", "   ", "   "]))
