class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs,ms = 0,float('-inf')
        for val in nums:
            cs += val
            ms = max(ms,cs)
            if cs < 0:
                cs = 0
        return ms