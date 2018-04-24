def grid():
    return [
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
    ]

def countIslands(grid):
    count    = 0
    rows     = len(grid)
    columns  = len(grid[0])
    used     = [[False for j in xrange(columns)] for i in xrange(rows)]

    for x in (xrange(rows)):
        for y in (xrange(columns)):
            if grid[x][y] == 1 and not used[x][y]:
                checkNeighbours(grid, used, rows, columns, x, y)
                count += 1
    return count

def checkNeighbours(grid, used, rows, columns, x, y):
    if grid[x][y] == 0 or used[x][y]:
        return
    used[x][y] = True

    if x != 0:
        checkNeighbours(grid, used, rows, columns, x - 1, y)
    if x != rows - 1:
        checkNeighbours(grid, used, rows, columns, x + 1, y)
    if y != 0:
        checkNeighbours(grid, used, rows, columns, x, y - 1)
    if y != columns -1:
        checkNeighbours(grid, used, rows, columns, x, y + 1)

print countIslands(grid())
