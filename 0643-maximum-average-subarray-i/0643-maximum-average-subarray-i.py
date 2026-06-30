class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        c_sum = sum(nums[:k])
        res = c_sum
        l = 0
        r = k
        while r <len(nums):
            c_sum += nums[r]
            c_sum -= nums[l]
            res = max(res,c_sum)
            l += 1
            r += 1
        return res/k