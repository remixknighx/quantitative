# -*- coding: utf-8 -*-
"""
946. Validate Stack Sequences
@link https://leetcode.com/problems/validate-stack-sequences/
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        empty_stack = []
        for push_word in pushed:
            empty_stack.append(push_word)
            if push_word == popped[0]:
                empty_stack.pop()
                popped.pop(0)
                while True:
                    if empty_stack and empty_stack[len(empty_stack) - 1] == popped[0]:
                        empty_stack.pop()
                        popped.pop(0)
                    else:
                        break
        return len(empty_stack) == 0 and len(popped) == 0


if __name__ == '__main__':
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(Solution().validateStackSequences(pushed=pushed, popped=popped))

    pushed2 = [1, 2, 3, 4, 5]
    popped2 = [4, 3, 5, 1, 2]
    print(Solution().validateStackSequences(pushed=pushed2, popped=popped2))
