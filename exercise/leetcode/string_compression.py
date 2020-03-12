# -*- coding: utf-8 -*-
"""
443. String Compression
@link https://leetcode.com/problems/string-compression/
"""
from typing import List
from collections import Counter


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars_count = Counter(chars)
        chars.clear()
        result = str()
        for (k, v) in enumerate(chars_count):
            if chars_count.get(v) == 1:
                result += v
            else:
                result += v
                result += str(chars_count.get(v))
        chars = list(result)
        print(chars)
        return len(result)


if __name__ == '__main__':
    chars = ["a","a","b","b","c","c","c"]
    print(Solution().compress(chars=chars))
