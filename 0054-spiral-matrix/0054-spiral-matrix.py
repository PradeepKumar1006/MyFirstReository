class Solution:
    def spiralOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        top = 0
        buttom = len(nums)-1
        left = 0
        right = len(nums[0])-1
        while left <= right and top <= buttom:
            for i in range(left,right+1):
                res.append(nums[top][i])
            top += 1
            for i in range(top,buttom+1):
                res.append(nums[i][right])
            right -= 1
            if top <= buttom:
                for i in range(right,left - 1,-1):
                    res.append(nums[buttom][i])
                buttom -= 1
            if left <= right:
                for i in range(buttom, top - 1, -1):
                    res.append(nums[i][left])
                left += 1

        return res
