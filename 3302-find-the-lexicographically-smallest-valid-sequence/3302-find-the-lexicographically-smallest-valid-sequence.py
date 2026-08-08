class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # dp[i] = maximum number of characters from word2
        # that can be matched exactly using word1[i:].
        dp = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                dp[i] += 1
                j -= 1

        # If word2 is already an exact subsequence,
        # greedy matching is enough.
        #
        # But we are allowed one mismatch.
        ans = []
        j = 0
        used = False

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed mismatch
            elif not used:
                # After using this mismatch, the remaining
                # word2[j+1:] must be exactly matchable.
                remaining = m - (j + 1)

                if dp[i + 1] >= remaining:
                    ans.append(i)
                    j += 1
                    used = True

        if j == m:
            return ans

        return []