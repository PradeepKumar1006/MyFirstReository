class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        ls = sorted(count.items(),key=lambda x: (-x[1],x[0]))
        return [word for word,f in ls[:k]]