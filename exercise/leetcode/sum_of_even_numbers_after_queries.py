# -*- coding: utf-8 -*-
"""
985. Sum of Even Numbers After Queries
@link https://leetcode.com/problems/sum-of-even-numbers-after-queries/
"""
from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result_list = []
        result = 0
        for num in A:
            if num % 2 == 0:
                result += num

        for query in queries:
            temp = A[query[1]] + query[0]
            if temp % 2 == 0:
                if A[query[1]] % 2 == 0:
                    result += query[0]
                else:
                    result += temp
            else:
                if A[query[1]] % 2 == 0:
                    result -= A[query[1]]
            A[query[1]] += query[0]
            result_list.append(result)

        return result_list


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    print(Solution().sumEvenAfterQueries(A=A, queries=queries))
