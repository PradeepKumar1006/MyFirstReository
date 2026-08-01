class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 in s2t and s2t[c1] != c2:
                return False
            if c2 in t2s and t2s[c2] != c1:
                return False
            s2t[c1] = c2
            t2s[c2] = c1
        return True