class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        k = len(s1)
        s1c = [0]*26
        s2c = [0]*26
        for ch in s1:
            s1c[ord(ch) - ord('a')] += 1
        for ch in s2[:k]:
            s2c[ord(ch) - ord('a')] += 1
        if s1c == s2c:
            return True
        for i in range(k,len(s2)):
            s2c[ord(s2[i]) - ord('a')] += 1
            s2c[ord(s2[i-k]) - ord('a')] -= 1

            if s1c == s2c:
                return True
        return False