class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = {}
        for s in strs:
            c = [0] * 26
            for ch in s:
                c[ord(ch) - ord('a')] += 1
            st = tuple(c)
            if st not in g:
                g[st] = []
            g[st].append(s)
        return list(g.values())