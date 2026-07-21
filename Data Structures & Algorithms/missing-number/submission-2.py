class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        elif len(nums) not in nums:
            return len(nums)
        
        all_nums: List[int] = [n for n in range(max(nums) + 1)]

        set_diff = set(all_nums) - set(nums)

        return list(set_diff)[0] if set_diff else None
