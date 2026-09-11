class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            ns = tuple(sorted(s))
            if ns not in dic:
                dic[ns] = []
            dic[ns].append(s)
        return list(dic.values())