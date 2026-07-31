class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1 = n2 = None
        c1 = c2 = 0
        n = len(nums)
        for val in nums:
            if n1 == val:
                c1 += 1
            elif n2 == val:
                c2 += 1
            elif c1 == 0:
                n1 = val
                c1 = 1
            elif c2 == 0:
                n2 = val
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        res = []
        if nums.count(n1) > n//3:
            res.append(n1)
        if n1 != n2 and nums.count(n2) > n//3:
            res.append(n2)
        return res