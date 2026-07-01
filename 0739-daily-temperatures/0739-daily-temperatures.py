class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        st = []
        for i in range(len(nums)):
            while st and nums[i] > nums[st[-1]]:
                j = st.pop()
                res[j] = i - j
            st.append(i)
        return res
