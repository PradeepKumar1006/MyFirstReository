class Solution:
    def wordPattern(self, pat: str, s: str) -> bool:
        l = s.split()
        if len(l) != len(pat):
            return False
        l2p = {}
        p2l = {}
        for i in range(len(l)):
            lc = l[i]
            pc = pat[i]
            if lc in l2p and l2p[lc] != pc:
                return False
            if pc in p2l and p2l[pc] != lc:
                return False
            l2p[lc] = pc
            p2l[pc] = lc
        return True