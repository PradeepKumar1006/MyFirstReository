class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        row = len(nums)
        col = len(nums[0])
        l = 0
        r = row * col- 1
        while l <= r:
            m = l + (r - l)//2
            ro = m//col
            c = m%col
            if nums[ro][c] == target:
                return True
            elif nums[ro][c] < target:
                l = m + 1
            else:
                r = m - 1
        return False