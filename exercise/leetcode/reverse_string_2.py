"""
541. Reverse String II
@link https://leetcode.com/problems/reverse-string-ii/
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result: str = ''
        for start in range(0, len(s), 2 * k):
            sub_s_length: int = len(s[start: start+2*k])
            if sub_s_length == 2 * k:
                result += s[start: start + k][::-1]
                result += s[start + k: start + 2 * k]
            elif k <= sub_s_length < 2 * k:
                result += s[start: start + k][::-1]
                result += s[start + k: start + sub_s_length]
            else:
                result += s[start: start + sub_s_length][::-1]
        return result


if __name__ == '__main__':
    s = 'abcdefg'
    print(Solution().reverseStr(s=s, k=2))

