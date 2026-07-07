class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return s

        start = 0
        max_len = 1

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(n):

            # Odd length palindrome
            l, r = expand(i, i)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l

            # Even length palindrome
            l, r = expand(i, i + 1)
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l

        return s[start:start + max_len]