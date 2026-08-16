class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        c0, c1, c2 = cnt

        # If there are no stones with remainder 1 or 2,
        # Alice cannot make a non-losing first move.
        if c1 == 0 and c2 == 0:
            return False

        # If c0 is even, Alice wins when both types 1 and 2 exist.
        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        # If c0 is odd, Alice needs an imbalance between
        # remainder-1 and remainder-2 stones.
        return abs(c1 - c2) > 2