import math

class Solution:
    def judgeSquareSum(self, n: int) -> bool:
        l = 0
        r = int(math.sqrt(n))

        while l <= r:
            s = l * l + r * r

            if s == n:
                return True
            elif s > n:
                r -= 1
            else:
                l += 1

        return False