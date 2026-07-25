class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for val in set(s):
            if s.count(val) != t.count(val):
                return False
        return True