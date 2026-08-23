class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = 1
        rp = 1
        n = len(nums)
        res = [1] * n
        for i in range(n):
            res[i] = lp
            lp *= nums[i]
        for i in range(n-1,-1,-1):
            res[i] *= rp
            rp *= nums[i]
        return res