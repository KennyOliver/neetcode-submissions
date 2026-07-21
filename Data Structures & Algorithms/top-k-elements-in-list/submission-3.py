class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Bucket sort based on frequencies
        bucket = [[] for _ in range(len(nums) + 1)]
        for nums_list, freq in freq_map.items():
            bucket[freq].append(nums_list)
        
        # Collect top K frequent elements
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
