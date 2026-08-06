class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s2t = {}
        t2s = {}
        for i in range(len(s)):
            se = s[i]
            te = t[i]
            if se in s2t and s2t[se] != te:
                return False
            if te in t2s and t2s[te] != se:
                return False
            s2t[se] = te
            t2s[te] = se
        return True