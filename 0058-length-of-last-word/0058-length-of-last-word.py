class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) -1
        res = ""
        while r >= 0 and s[r] == ' ':
            r -= 1
        while r >= 0 and s[r] != ' ':
            res += s[r]
            r -= 1
        return len(res)