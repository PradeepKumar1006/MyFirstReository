class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        for val in nums:
            dic[val] = dic.get(val,0)+1
        res = []
        for key in dic.keys():
            if dic[key] > len(nums)//3:
                res.append(key)
        return res