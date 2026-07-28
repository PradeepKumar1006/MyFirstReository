class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for val in nums:
            if val == 0:
                nums.remove(val)
                nums.append(val)
        