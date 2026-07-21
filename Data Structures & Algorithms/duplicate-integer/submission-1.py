class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            if not num in num_count:
                num_count[num] = 1
            else:
                num_count[num] = num_count[num] + 1
        
        for key, val in num_count.items():
            if val > 1:
                return True
        
        return False
