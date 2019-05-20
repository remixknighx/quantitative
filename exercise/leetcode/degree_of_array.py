# -*- coding: utf-8 -*-

"""
697. Degree of an Array
@link https://leetcode.com/problems/degree-of-an-array/
"""
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        result_dict = dict()
        for i in range(0, len(nums)):
            if result_dict.get(nums[i]) is None:
                # [1, i, i] 0位表示出现次数，1位表示起始位置，2位表示结束位置
                result_dict[nums[i]] = [1, i, i]
            else:
                num_temp = result_dict.get(nums[i])
                num_temp[0] += 1
                num_temp[2] = i

        shortest_length: int = 50000
        maxest_occur: int = 0
        for key in result_dict.keys():
            if result_dict.get(key)[0] > maxest_occur:
                maxest_occur = result_dict.get(key)[0]
                shortest_length = result_dict.get(key)[2] - result_dict.get(key)[1] + 1
            elif result_dict.get(key)[0] == maxest_occur:
                shortest_length = min(result_dict.get(key)[2] - result_dict.get(key)[1] + 1, shortest_length)
        return shortest_length


if __name__ == '__main__':
    num_list = list()
    num_list.append(1)
    num_list.append(2)
    num_list.append(2)
    num_list.append(3)
    num_list.append(1)
    num_list.append(4)
    num_list.append(2)
    print(Solution().findShortestSubArray(nums=num_list))

