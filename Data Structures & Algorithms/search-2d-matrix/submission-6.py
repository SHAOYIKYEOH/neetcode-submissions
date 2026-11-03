class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = 0
        COLS = len(matrix[0])

        top = 0
        bot = len(matrix) - 1
        

        while top <= bot:
            m = (top + bot) // 2
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bot = m - 1
            else:
                break

        if not (top <= bot):
            return False

        l,r = 0, COLS-1
        m = (top + bot) // 2
        
        while l <= r:
            m2 = (l + r) //2
            if target > matrix[m][m2]:
                l = m2 + 1
            elif target < matrix[m][m2]:
                r = m2 - 1
            elif target == matrix[m][m2]:
                return True
        return False

                   
        