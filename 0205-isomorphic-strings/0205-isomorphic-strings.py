class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            s1 = s[i]
            t1 = t[i]
            if s1 in s2t and s2t[s1] != t1:
                return False
            if t1 in t2s and t2s[t1] != s1:
                return False
            s2t[s1] = t1
            t2s[t1] = s1
        return True