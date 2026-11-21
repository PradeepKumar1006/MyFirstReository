class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in dic:
                return [i,dic[d]]
            else:
                dic[nums[i]] = i
        return None