class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        t = sum(nums)
        ls = 0
        for i in range(n):
            rs = t - ls - nums[i]
            if rs == ls:
                return i
            else:
                ls += nums[i]
        return -1