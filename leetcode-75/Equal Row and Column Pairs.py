
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        equalRow = Counter()
        count = 0

        for i in grid:
            equalRow[tuple(i)]+=1
        
        for j in range(len(grid[0])):

            col = [grid[i][j] for i in range(len(grid))]
            count+=equalRow[tuple(col)]
        
        return count



        
         


        
