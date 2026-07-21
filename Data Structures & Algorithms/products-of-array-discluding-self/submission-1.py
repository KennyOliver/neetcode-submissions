class Solution:
    def helperEditedArray(self, nums: List[int], i: int) -> List[int]:
        return nums[:i] + nums[i+1:]
    
    def helperProductArray(self, nums: List[int]) -> int:
        product_result = 1
        for n in nums:
            product_result *= n

        return product_result

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range (0, len(nums)):
            result.append(self.helperProductArray(self.helperEditedArray(nums, i)))
        
        return result
