from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        arr.sort(key=cmp_to_key(compare))

        res = "".join(arr)

        return "0" if res[0] == "0" else res