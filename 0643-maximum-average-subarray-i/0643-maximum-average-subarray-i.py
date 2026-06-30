class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cs = sum(nums[:k])
        ms = cs
        i = 0
        j = k
        while j < len(nums):
            cs += nums[j]
            cs -= nums[i]
            ms = max(ms, cs)
            i += 1
            j += 1
        return ms / k