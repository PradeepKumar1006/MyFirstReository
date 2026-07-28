class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        for val in nums:
            if val < res:
                res = val
        return res