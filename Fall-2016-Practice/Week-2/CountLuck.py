tests = int(input())

for test in range(tests):
    n, m = map(int, input().split())
    grid = [input() for i in range(n)]
    k = int(input())
    
    start = (-1, -1)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'M':
                start = (i, j)

    visited = [[None for i in range(m)] for j in range(n)]
    stack = [start]

    while len(stack) > 0:
        point = stack.pop()
        x = point[0]
        y = point[1]
        
        if grid[x][y] == '*':
            decisions = 0
            while True:
                point =  visited[x][y]
                x = point[0]
                y = point[1]
                
                degree = 0
                if x > 0 and not grid[x - 1][y] == 'X':
                    degree += 1

                if x < n - 1 and not grid[x + 1][y] == 'X':
                    degree += 1

                if y > 0 and not grid[x][y - 1] == 'X':
                    degree += 1

                if y < m - 1 and not grid[x][y + 1] == 'X':
                    degree += 1

                if degree > 2:
                    decisions += 1

                if grid[x][y] == 'M':
                    if degree == 2:
                        decisions += 1
                    if decisions == k:
                        print('Impressed')
                    else:
                        print('Oops!')
                    break

        if x > 0 and not visited[x - 1][y] and not grid[x - 1][y] == 'X':
            visited[x - 1][y] = (x, y)
            stack.append((x - 1, y))

        if x < n - 1 and not visited[x + 1][y] and not grid[x + 1][y] == 'X':
            visited[x + 1][y] = (x, y)
            stack.append((x + 1, y))

        if y > 0 and not visited[x][y - 1] and not grid[x][y - 1] == 'X':
            visited[x][y - 1] = (x, y)
            stack.append((x, y - 1))

        if y < m - 1 and not visited[x][y + 1] and not grid[x][y + 1] == 'X':
            visited[x][y + 1] = (x, y)
            stack.append((x, y + 1))
