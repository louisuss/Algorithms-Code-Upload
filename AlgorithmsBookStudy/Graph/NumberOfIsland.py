n = int(input())
islands = [list(map(int, list(input()))) for _ in range(n)]

def numIsLands(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 0
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i,j)
                cnt += 1
    return cnt

print(numIsLands(islands))



# class Solution:
#     def dfs(self, grid, i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
#             return

#         grid[i][j] = 0
#         self.dfs(grid, i+1, j)
#         self.dfs(grid, i, j+1)
#         self.dfs(grid, i-1, j)
#         self.dfs(grid, i, j-1)

#     def numIsLands(self, grid):
#         if not grid:
#             return 0

#         cnt = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     self.dfs(grid, i, j)
#                     cnt += 1
#         return cnt
    
        
