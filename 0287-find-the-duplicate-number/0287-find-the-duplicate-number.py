class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sett = set()
        for val in nums:
            if val in sett:
                return val
            sett.add(val)
        return -1