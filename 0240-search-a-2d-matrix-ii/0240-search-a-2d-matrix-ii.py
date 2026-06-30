class Solution:
    def searchMatrix(self, nums: List[List[int]], target: int) -> bool:
        for rows in nums:
            if target in rows:
                return True
        return False