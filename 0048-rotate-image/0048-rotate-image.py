class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        n = len(nums)
        m = len(nums[0])
        for i in range(n):
            for j in range(i+1,m):
                nums[i][j],nums[j][i] = nums[j][i],nums[i][j]
        for row in nums:
            row.reverse()