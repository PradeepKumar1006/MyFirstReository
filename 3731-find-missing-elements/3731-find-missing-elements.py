class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        res = []

        for num in range(min(nums), max(nums)):
            if num not in s:
                res.append(num)

        return res