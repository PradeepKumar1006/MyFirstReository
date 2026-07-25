class Solution:
    def maxProduct(self, n: int) -> int:
        res = float('-inf')
        arr = list(str(n))
        arr.sort()
        for i in range(1,len(arr)):
            res = max(res, int(arr[i]) * int(arr[i-1]))
        return res