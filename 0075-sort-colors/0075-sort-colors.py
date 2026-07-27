class Solution:
    def sortColors(self, nums: List[int]) -> None:
        oc = sc = tc = 0
        for val in nums:
            if val == 0:
                oc += 1
            elif val == 1:
                sc += 1
            else:
                tc += 1
        i = 0
        while oc > 0:
            nums[i] = 0
            i += 1
            oc -= 1
        while sc > 0:
            nums[i] = 1
            i += 1
            sc -= 1
        while tc > 0:
            nums[i] = 2
            i += 1
            tc -= 1