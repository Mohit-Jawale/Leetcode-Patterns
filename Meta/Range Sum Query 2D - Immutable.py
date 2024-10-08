class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        if not matrix or not matrix[0]:
            return
        row,col  = len(matrix),len(matrix[0])
        self.dp = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.dp[i][j] = matrix[i-1][j-1] + self.dp[i-1][j]+ self.dp[i][j-1]-self.dp[i-1][j-1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
