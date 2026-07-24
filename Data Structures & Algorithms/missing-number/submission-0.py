class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        
        all_nums: List[int] = [n for n in range(max(nums) + 1)]
        return list(set(all_nums) - set(nums))[0]