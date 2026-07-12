class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for val in nums:
            dic[val] = dic.get(val,0)+1
        res = []
        for key in dic.keys():
            if dic[key] == 1:
                res.append(key)
        return res