class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        top = 0
        bottom = rows - 1

        while top <= bottom:
            m = (top + bottom) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                row = m
                break
        else:
            return False

        nums = matrix[row]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m2 = (l+r) // 2
            if target > nums[m2]:
                l = m2 + 1
            elif target < nums[m2]:
                r = m2 - 1
            else:
                return True
        return False


        