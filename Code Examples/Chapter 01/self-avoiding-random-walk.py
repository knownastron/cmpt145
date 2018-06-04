"""
CMPT 145 Computing with Python Lists
Self-Avoiding Random Walk

Given an n by n grid.  Start at the center of the grid, repeatedly
take random steps in any of the 4 cardinal directions, without stepping
onto a location that has already been visited.  It's a win to get to a
border (escape), and a loss if you can't move (dead-end).

What is the probability of reaching a dead-end?
"""

import random as random

n = 101            # grid width and height
trials = 10000      # number of trials to run


dead_ends = 0       # count of dead ends (failures) across all trials

def SARW(n):
    """
    A single trial of a self-avoiding random walk in an n x n room until
    walker reaches a wall (success) or dead end (failure).
    n: number of possible steps
    return: the outcome of the trial (True for success, False for failure)
    """
    
    reached_dead_end = False  # whether we reached a dead end

    # initialize n by n grid of locations visited where ith location is
    # True if walker stepped there previously (all initially not visited)
    a = [[False for y in range(n)] for x in range(n)]

    # set up walker to start in center of grid
    x = n // 2  # walker's x-coordinate
    y = n // 2  # walker's y-coordinate

    # continue walking randomly until a wall is reached (success)
    # or a location must be revisited (failure)
    while (not reached_dead_end) and (x > 0 and x < n-1 and y > 0 and y < n-1):

        # we are currently visiting (x,y)
        a[x][y] = True

        # check to see if walker must revisit location (failure)
        # if so, mark dead end and end trial
        if a[x-1][y] and a[x+1][y] and a[x][y-1] and a[x][y+1]:
            reached_dead_end = True

        # randomly walk in an available cardinal direction
        r = random.randrange(1,5)  # cardinal direction to walk in
        if   r == 1 and not a[x+1][y]: x += 1  # east
        elif r == 2 and not a[x-1][y]: x -= 1  # west
        elif r == 3 and not a[x][y+1]: y += 1  # south
        elif r == 4 and not a[x][y-1]: y -= 1  # north

    # return True if we have reached a wall successfully (i.e. not a dead end)
    return not reached_dead_end


# for every trial, track whether it ends in success or failure
for t in range(trials):
    success = SARW(n)
    if not success:
        dead_ends += 1

# display percentage of dead ends reached in all trials
print(str(100*dead_ends / trials) + '% dead ends')
