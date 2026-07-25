class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for val in sett:
            if val - 1 not in sett:
                l = 1
                while val+l in sett:
                    l += 1
                res = max(res,l)
        return res