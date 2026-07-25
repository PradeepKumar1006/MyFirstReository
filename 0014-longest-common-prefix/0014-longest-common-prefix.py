class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        res = ''
        f = strs[0]
        l = strs[-1]
        for i in range(min(len(f),len(l))):
            if f[i] != l[i]:
                break
            res += f[i]
        return res