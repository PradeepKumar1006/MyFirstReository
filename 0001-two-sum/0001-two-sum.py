class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in dic:
                return [dic[d],i]
            else:
                dic[nums[i]] = i
        return [-1,-1]