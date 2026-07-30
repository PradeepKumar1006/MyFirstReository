class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        sl = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        return [word for word, freq in sl[:k]]