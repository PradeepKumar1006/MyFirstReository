import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l ,r = 1,max(piles)
        while l < r:
            m = l + (r-l)//2
            hr = 0
            for b in piles:
                hr += math.ceil(b/m)
            if hr <= h:
                r = m
            else:
                l = m+1
        return l