class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sl = sorted(count.items(),key=lambda x:x[1],reverse=True)
        return [num for num,fre in sl[:k]]