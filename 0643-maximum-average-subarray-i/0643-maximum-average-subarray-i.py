class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        ms = cur_sum
        l , r = 0,k
        while r <len(nums):
            cur_sum += nums[r] - nums[l]
            ms = max(ms,cur_sum)
            l += 1
            r += 1
        return ms/k