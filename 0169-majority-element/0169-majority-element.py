class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = None
        count = 0
        for val in nums:
            if count == 0:
                num = val
            if val == num:
                count += 1
            else:
                count -= 1
        return num