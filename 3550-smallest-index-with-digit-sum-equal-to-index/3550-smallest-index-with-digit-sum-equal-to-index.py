class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum = 0
            n = nums[i]
            while n:
                sum += n%10
                n //= 10
            if sum == i:
                return i
        return -1