class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s)
        tc = Counter(t)
        for ch in tc:
            if tc[ch] > sc[ch]:
                return ch