class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float('-inf')
        while l < r:
            res = max(res,(min(nums[l],nums[r])*(r-l)))
            if nums[l] < nums[r]:
                l += 1
            else:
                r -= 1
        return res