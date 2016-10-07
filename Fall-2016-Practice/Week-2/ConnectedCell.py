def getBiggestRegion(grid):
    width = len(grid)
    height = len(grid[0])
    found = [[False for i in range(height)] for i in range(width)]
    maxSize = 0
    for i in range(width):
        for j in range(height):
            size = 0
            if grid[i][j] == 1 and not found[i][j]:
                size = explore(grid, found, i, j)
                if size > maxSize:
                    maxSize = size
    return maxSize
                    
def explore(grid, found, i, j):
    numExplored = 0
    toExplore = [(i, j)]
    width = len(grid)
    height = len(grid[0])
    while len(toExplore) > 0:
        nextExplore = toExplore.pop()
        x = nextExplore[0]
        y = nextExplore[1]
        if not found[x][y]:
            found[x][y] = True
            numExplored += 1
            for xDiff in range(-1, 2):
                for yDiff in range(-1, 2):
                    if 0 <= x + xDiff and x + xDiff <= width - 1 and 0 <= y + yDiff and y + yDiff <= height - 1:
                        if grid[x + xDiff][y + yDiff] == 1 and not found[x + xDiff][y + yDiff]:
                            toExplore.append((x + xDiff, y + yDiff))
        
    return numExplored
            
n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
