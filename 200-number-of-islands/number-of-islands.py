class Solution(object):
    def numIslands(self, grid):
        height = len(grid)
        length = len(grid[0])
        visited_array = [[0 for i in range(length)] for x in range(height)]
        count = 0
        for i in range(len(grid)):
            for x in range(len(grid[0])):
                # find starting point
                # use stack and visited map
                stack = []
                if grid[i][x] == "1" and visited_array[i][x]==0:
                    count += 1
                    stack.append([i,x])
                    # while the stack isn't empty
                    while stack:
                        popped = stack.pop()
                        a = popped[0]
                        b = popped[1]
                        # mark as seen
                        visited_array[a][b] = 1

                        # add to stack the children
                        
                        if a < height-1 and grid[a+1][b] == "1" and visited_array[a+1][b] == 0:
                            stack.append([a+1,b])
                        if a > 0 and grid[a-1][b]  == "1" and visited_array[a-1][b] == 0:
                            stack.append([a-1,b])
                        if b < length-1 and grid[a][b+1] == "1" and visited_array[a][b+1] == 0:
                            stack.append([a,b+1])      
                        if b > 0 and grid[a][b-1] == "1" and visited_array[a][b-1] == 0:
                            stack.append([a,b-1])
                           
        return count