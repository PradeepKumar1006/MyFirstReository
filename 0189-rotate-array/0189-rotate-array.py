class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        s = nums[:(n-k)]
        f = nums[(n-k):]
        r = f + s
        for i in range(n):
            nums[i] = r[i]