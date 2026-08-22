class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        t = n
        while n:
            last = n%10
            s += last
            p *= last
            n //= 10
        return t%(s+p)==0