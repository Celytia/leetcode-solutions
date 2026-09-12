class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col=[]
        row=[]
        i=j=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    col.append(j)
                    row.append(i)
                    continue
        for m in range(len(matrix)):
            if m in row:
                for n in range(len(matrix[0])):
                    matrix[m][n]=0
        for m in range(len(matrix[0])):
            if m in col:
                for n in range(len(matrix)):
                    matrix[n][m]=0
        return matrix