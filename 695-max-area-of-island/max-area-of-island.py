class Solution(object):
    def maxAreaOfIsland(self, grid):
        height = len(grid)
        width = len(grid[0])
        
        seen_grid = [[0 for _ in range(width)] for __ in range(height)]
        # m for max
        m = 0
        for a in range(height):
            for b in range(width):
                
                stack = []
                if grid[a][b] == 1 and seen_grid[a][b] == 0:
                    stack.append([a,b])
                    temp_count = 1
                    # we saw it
                    seen_grid[a][b] = 1
                    while stack:
                        v = stack.pop()
                        i = v[0]
                        x = v[1]
                        if i > 0 and grid[i-1][x] == 1 and seen_grid[i-1][x] == 0:
                            seen_grid[i-1][x] = 1
                            stack.append([i-1,x])
                            temp_count += 1
                        if i < height-1 and grid[i+1][x] == 1 and seen_grid[i+1][x] == 0:
                            seen_grid[i+1][x] = 1
                            stack.append([i+1,x])
                            temp_count += 1
                        if x > 0 and grid[i][x-1] == 1 and seen_grid[i][x-1] == 0:
                            seen_grid[i][x-1] = 1
                            stack.append([i,x-1])
                            temp_count += 1
                        if x < width-1 and grid[i][x+1] == 1 and seen_grid[i][x+1] == 0:
                            seen_grid[i][x+1] = 1
                            stack.append([i,x+1])
                            temp_count += 1
                    m = max(m,temp_count)
        return m
                                            
