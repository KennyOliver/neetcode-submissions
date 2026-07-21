class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = -1
        b = -1

        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    a = i
                    b = j
                    break
        
        if -1 not in (a, b):
            return [a, b] if a < b else [b, a]
        else:
            return []
