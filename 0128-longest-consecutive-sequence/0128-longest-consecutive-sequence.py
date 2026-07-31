class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        res = 0
        for num in sett:
            if num - 1 not in sett:
                l = 0
                while num+l in sett:
                    l += 1
                res = max(res,l)
        return res