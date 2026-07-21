class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Multiply smaller of two heights, with distance between
        # Therefore (width = i_end - i_start) and (height = min(height1, height2))

        # candidate1 = None
        # candidate2 = None
        largest_area_found = 0

        for i in range(0, len(heights)):
            for j in range(i, len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                largest_area_found = max(largest_area_found, area)
        
        return largest_area_found
        