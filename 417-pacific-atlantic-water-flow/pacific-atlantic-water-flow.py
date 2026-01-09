class Solution(object):
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return []
            
        height = len(heights)
        width = len(heights[0])

        pacific = [[0 for _ in range(width)] for __ in range(height)]
        atlantic = [[0 for _ in range(width)] for __ in range(height)]
        
        pac_stack = []
        atl_stack = []

        for c in range(width):
            pac_stack.append([0, c])
            pacific[0][c] = 1
        for r in range(1, height):
            pac_stack.append([r, 0])
            pacific[r][0] = 1

        for c in range(width):
            atl_stack.append([height - 1, c])
            atlantic[height - 1][c] = 1
        for r in range(0, height - 1):
            atl_stack.append([r, width - 1])
            atlantic[r][width - 1] = 1

        while pac_stack:
            a, b = pac_stack.pop()
            # Check Up
            if a > 0 and pacific[a-1][b] == 0 and heights[a-1][b] >= heights[a][b]:
                pacific[a-1][b] = 1
                pac_stack.append([a-1, b])
            # Check Down
            if a < height - 1 and pacific[a+1][b] == 0 and heights[a+1][b] >= heights[a][b]:
                pacific[a+1][b] = 1
                pac_stack.append([a+1, b])
            # Check Left
            if b > 0 and pacific[a][b-1] == 0 and heights[a][b-1] >= heights[a][b]:
                pacific[a][b-1] = 1
                pac_stack.append([a, b-1])
            # Check Right
            if b < width - 1 and pacific[a][b+1] == 0 and heights[a][b+1] >= heights[a][b]:
                pacific[a][b+1] = 1
                pac_stack.append([a, b+1])

        while atl_stack:
            a, b = atl_stack.pop()
            # Check Up
            if a > 0 and atlantic[a-1][b] == 0 and heights[a-1][b] >= heights[a][b]:
                atlantic[a-1][b] = 1
                atl_stack.append([a-1, b])
            # Check Down
            if a < height - 1 and atlantic[a+1][b] == 0 and heights[a+1][b] >= heights[a][b]:
                atlantic[a+1][b] = 1
                atl_stack.append([a+1, b])
            # Check Left
            if b > 0 and atlantic[a][b-1] == 0 and heights[a][b-1] >= heights[a][b]:
                atlantic[a][b-1] = 1
                atl_stack.append([a, b-1])
            # Check Right
            if b < width - 1 and atlantic[a][b+1] == 0 and heights[a][b+1] >= heights[a][b]:
                atlantic[a][b+1] = 1
                atl_stack.append([a, b+1])

        rl = []
        for r in range(height):
            for c in range(width):
                if pacific[r][c] == 1 and atlantic[r][c] == 1:
                    rl.append([r, c])
        
        return rl