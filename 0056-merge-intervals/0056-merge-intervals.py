class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for s,e in intervals[1:]:
            las_end = res[-1][1]
            if s <= las_end:
                res[-1][1] = max(las_end,e)
            else:
                res.append([s,e])
        return res