class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        r = len(nums)
        c = len(nums[0])
        l = 0
        r = r * c -1
        while l <= r:
            m = l + (r-l)//2
            rp = m//c
            cp = m%c
            if nums[rp][cp] == target:
                return True
            elif nums[rp][cp] < target:
                l = m + 1
            else:
                r = m - 1
        return False