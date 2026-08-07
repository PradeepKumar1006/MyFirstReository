class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)

        while l < r:

            m = l + (r-l)//2

            need = 1
            curr = 0

            for w in weights:

                if curr + w <= m:
                    curr += w
                else:
                    need += 1
                    curr = w

            if need <= days:
                r = m
            else:
                l = m + 1

        return l