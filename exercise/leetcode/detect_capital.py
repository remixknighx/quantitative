"""
520. Detect Capital
@link https://leetcode.com/problems/detect-capital/
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        count: int = 0
        for index in range(1, len(word)):
            if ord(word[index]) >= 65 and ord(word[index]) <= 90:
                count += 1

        if ord(word[0]) >= 65 and ord(word[0]) <= 90:
            if count == len(word) - 1 or count == 0:
                return True
            else:
                return False
        elif (ord(word[0]) < 65 or ord(word[0]) > 90) and count == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().detectCapitalUse('USA'))
    print(Solution().detectCapitalUse('leetcode'))
    print(Solution().detectCapitalUse('Google'))
    print(Solution().detectCapitalUse('GooDle'))
    print(Solution().detectCapitalUse('oD'))
