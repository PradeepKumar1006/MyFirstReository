class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in dic:
                return [i,dic[dif]]
            else:
                dic[nums[i]] = i
        return []