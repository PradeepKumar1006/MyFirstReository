class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def fs():
            l , r = 0, len(nums)-1
            ans = -1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    ans = m
                    r = m - 1
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m - 1
            return ans
        def ss():
            l , r = 0, len(nums)-1
            ans = -1
            while l <= r:
                m = l + (r-l)//2
                if nums[m] == target:
                    ans = m
                    l = m + 1
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m - 1
            return ans
        return [fs(),ss()]