class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = list(map(lambda x: x*x,nums))
        res.sort()
        return res