class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = None
        c = 0
        for val in nums:
            if c == 0:
                can = val
            if can == val:
                c += 1
            else:
                c -= 1
        return can