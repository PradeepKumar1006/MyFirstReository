class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        res = 0
        while s[n] == ' ':
                n -= 1
        while n >= 0 and s[n] != ' ':
            res += 1
            n -= 1
        return res
