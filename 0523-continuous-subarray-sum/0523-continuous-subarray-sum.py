class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k

            if rem in mp:
                if i - mp[rem] >= 2:
                    return True
            else:
                mp[rem] = i

        return False