# -*- coding: utf-8 -*-
"""
1313. Decompress Run-Length Encoded List
@link https://leetcode.com/problems/decompress-run-length-encoded-list/
"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            for count in range(0, nums[i]):
                result.append(nums[i+1])
        return result


if __name__ == '__main__':
    print(Solution().decompressRLElist(nums=[1, 2, 3, 4]))
    print(Solution().decompressRLElist(nums=[1, 1, 2, 3]))
