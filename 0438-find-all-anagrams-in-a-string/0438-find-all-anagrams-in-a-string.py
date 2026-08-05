class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        res = []
        k = len(p)
        sc = [0]*26
        wc = [0]*26
        for ch in p:
            sc[ord(ch) - ord('a')] += 1
        for ch in s[:k]:
            wc[ord(ch) - ord('a')] += 1
        if wc == sc:
            res.append(0)
        for i in range(k,len(s)):
            wc[ord(s[i]) - ord('a')] += 1
            wc[ord(s[i-k]) - ord('a')] -= 1

            if sc == wc:
                res.append(i-k+1)
        return res