"""
561. Array Partition 1
@link https://leetcode.com/problems/array-partition-i/
"""

from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result: int = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


if __name__ == '__main__':
    nums: List = [1, 4, 3, 2]
    print(Solution().arrayPairSum(nums=nums))
