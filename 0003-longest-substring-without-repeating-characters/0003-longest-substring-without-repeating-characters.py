class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        res = 0
        i = 0
        for j in range(len(s)):
            while s[j] in sett:
                sett.remove(s[i])
                i += 1
            sett.add(s[j])
            res = max(res,j-i+1)
        return res