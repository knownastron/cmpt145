# Mike's quick and dirty solution to A7Q7
# doesn't read the maze files yet!

grid = [[0, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]]

gridlines =  [
        '0 0 0 0 0 1 0 0',
        '1 0 1 1 0 0 0 0',
        '1 0 0 1 0 1 0 1',
        '0 1 0 0 0 1 0 0',
        '0 0 0 0 1 1 0 1',
        '0 0 1 0 0 0 0 0'
        ]

grid2 = [[int(x) for x in line.split()] for line in gridlines]


def search(grid, x, y, tx, ty, allSolutions=False):
    # internal defs FTW
    def do_search(x, y):
        if x == tx and y == ty:
            # arrived at the target; mark it visited
            grid[x][y] = 3
            # display to the console
            for line in grid:
                print(line)
            print('-------------')
            return not allSolutions
        elif grid[x][y] == 1:
            # can't occupy a wall
            return False
        elif grid[x][y] == 3:
            # can't return to a visited node
            return False

        # mark as visited
        grid[x][y] = 3

        # explore neighbors clockwise starting by the one on the right
        if ((x < len(grid)-1 and do_search(x+1, y,))
            or (y > 0 and do_search(x, y-1))
            or (x > 0 and do_search(x-1, y))
            or (y < len(grid[0])-1 and do_search(x, y+1))):
            return True

        # if we get here, the visit was unsuccessful, so unmark
        grid[x][y] = 0
        return False

    return do_search(x, y)

search(grid, 0, 0, 5, 5, allSolutions=True)
search(grid2, 0, 0, 5, 7)
