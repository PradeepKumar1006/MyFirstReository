class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res ^= val
        return res