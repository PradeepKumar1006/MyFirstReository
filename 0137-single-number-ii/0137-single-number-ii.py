class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for val in nums:
            dic[val] = dic.get(val,0)+1
        for key in dic.keys():
            if dic[key] == 1:
                return key