class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            for val in row:
                if val < 0:
                    res += 1
        return res