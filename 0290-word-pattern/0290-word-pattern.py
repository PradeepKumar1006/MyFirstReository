class Solution:
    def wordPattern(self, pat: str, s: str) -> bool:
        ls = s.split()
        if len(ls) != len(pat):
            return False
        l2p = {}
        p2l = {}
        for i in range(len(ls)):
            lse = ls[i]
            pate = pat[i]
            if lse in l2p and l2p[lse] != pate:
                return False
            if pate in p2l and p2l[pate] != lse:
                return False
            l2p[lse] = pate
            p2l[pate] = lse
        return True