class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sl = sorted(count.items(), key= lambda x: x[1], reverse=True)
        return [n for n,f in sl[:k]]