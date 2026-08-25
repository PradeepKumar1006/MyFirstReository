class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        sett = set(nums)
        i = k
        while True:
            if i not in sett: return i
            else: i += k