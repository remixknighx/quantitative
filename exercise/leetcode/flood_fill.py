# -*- coding: utf-8 -*-
"""
733. Flood Fill
@link https://leetcode.com/problems/flood-fill/
"""
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]
        if orig_color != newColor:
            traverse(sr, sc)
        return image


if __name__ == '__main__':
    image:List = []
    image.append([1, 1, 1])
    image.append([1, 1, 0])
    image.append([1, 0, 1])
    print(Solution().floodFill(image=image, sr=1, sc=1, newColor=2))