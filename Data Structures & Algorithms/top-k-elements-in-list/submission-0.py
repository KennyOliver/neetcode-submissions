class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: Dict[int, List[int]] = {}
        for num in nums:
            c = nums.count(num)
            if c not in counts:
                counts[c] = [num]
            else:
                counts[c].append(num)
        sorted_counts = sorted(counts.items(), key=lambda x: x[0], reverse=True)
        result = [x[1][0] for x in sorted_counts[:k]]
        return result
