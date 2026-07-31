class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s) - 1

        # Skip trailing spaces
        while r >= 0 and s[r] == ' ':
            r -= 1

        count = 0

        # Count characters of the last word
        while r >= 0 and s[r] != ' ':
            count += 1
            r -= 1

        return count