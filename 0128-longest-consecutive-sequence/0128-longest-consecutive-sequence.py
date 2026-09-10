class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for val in seen:
            if val - 1 not in seen:
                l = val

                while l + 1 in seen:
                    l += 1

                res = max(res, l - val + 1)

        return res