# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text_list = text.split(' ')
        for i in range(0, len(text_list)-2):
            if text_list[i] == first and text_list[i+1] == second:
                result.append(text_list[i+2])
        return result


if __name__ == '__main__':
    text = 'alice is a good girl she is a good student'
    first = 'a'
    second = 'good'
    print(Solution().findOcurrences(text=text, first=first, second=second))