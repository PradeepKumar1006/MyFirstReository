class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) -1 
        res = 0
        while r >=0 and s[r] == ' ':
            r -= 1
        while r >= 0 and s[r] != ' ':
            res += 1
            r -= 1
        return res