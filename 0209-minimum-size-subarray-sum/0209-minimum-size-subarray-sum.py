class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        cs = 0
        ml = float('inf')
        for r in range(n):
            cs += nums[r]

            while cs >= target:
                ml = min(ml,r-l+1)
                cs -= nums[l]
                l += 1
        return ml if ml != float('inf') else 0