class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0, len(matrix)):
            # if matrix[i][0] == target:
            #     return True
            # else:
            if target in matrix[i]:
                return True
            else:
                continue
        
        return False
        