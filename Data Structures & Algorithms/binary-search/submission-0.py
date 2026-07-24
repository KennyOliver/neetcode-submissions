class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        low, high = 0, (len(nums) - 1)
        found = False

        while not found:
            mid = round((low + high) / 2)
            if nums[mid] == target:
                result = mid
                found = True
            elif nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
            else:
                if low == mid == high and mid != target:
                    break
        
        return result
        