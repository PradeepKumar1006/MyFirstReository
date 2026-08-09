class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        # dp(i, M) = maximum stones current player can get
        # starting from index i with current M
        memo = {}

        def dp(i, M):
            if i >= n:
                return 0

            if (i, M) in memo:
                return memo[(i, M)]

            best = 0

            # Take X piles, where 1 <= X <= 2*M
            for X in range(1, 2 * M + 1):
                if i + X > n:
                    break

                # Stones remaining after taking X piles
                remaining = suffix[i + X]

                # Opponent gets the best they can get
                opponent = dp(i + X, max(M, X))

                # Current player gets everything remaining
                # minus what opponent can eventually get
                current = suffix[i] - opponent

                best = max(best, current)

            memo[(i, M)] = best
            return best

        return dp(0, 1)