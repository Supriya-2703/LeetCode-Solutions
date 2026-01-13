class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        row0_zero = False
        col0_zero = False
        
        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                col0_zero = True
        
        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                row0_zero = True
        
        # Use first row & column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero first column
        if col0_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        # Zero first row
        if row0_zero:
            for j in range(n):
                matrix[0][j] = 0
