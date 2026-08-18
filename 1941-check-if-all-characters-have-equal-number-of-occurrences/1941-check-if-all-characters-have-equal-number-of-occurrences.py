class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        l = len(set(count.values()))
        return l==1