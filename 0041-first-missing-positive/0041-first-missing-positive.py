class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sett = set(nums)
        i = 1
        while True:
            if i not in sett:
                return i
            else:
                i += 1