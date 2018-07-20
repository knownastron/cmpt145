#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

def get_maze(maze_name):
    """
    Purpose:
        takes in a name of a txt file and outputs a list of list where each line
        is a list within the outer list, and each character seperated by a space
        is an element within the inner list
    Pre-conditions:
        :param maze_name: Must be a string in the form 'xxxxx.txt'.
                          Text file should contain 1 and 0 seperated by spaces.
                          Each line in the text file should have the same number
                          of characters
    return:

    """
    maze = []
    lines_list = open(maze_name).read().splitlines()
    for line in lines_list:
        maze.append(line.split())
    return maze

def MazeSolver(m, s, g):
    """
    Purpose:
        Takes in a maze, a starting location, and an goal location. Returns
        whether a path can be found from the start to the goal
    Pre-conditions:
        :param m: a list of lists where each element in the inner list is a '1'
                  or '0'
    Post-condition:
        if a path is found from start to goal, the path taken will replace '0'
        with 'P'
    return:
        True if a path is found from s to g, false otherwise
    """
    val = m[s[0]][s[1]]
    if val == '0' and s == g:
        m[s[0]][s[1]] = 'P'
        print_maze(m)
        return True
    elif val == '1':
        return False
    else:
        east, south, west, north = False, False, False, False
        found_path = east or south or west or north

        m[s[0]][s[1]] = 'P'

        if s[0] != 0 and found_path == False:
            new_n = (s[0] - 1, s[1])
            if m[new_n[0]][new_n[1]] != 'P':
                north = MazeSolver(m, new_n, g)
            else:
                pass
        if s[1] != 0 and found_path == False:
            new_w = (s[0], s[1]-1)
            if m[new_w[0]][new_w[1]] != 'P':
                west = MazeSolver(m, new_w, g)
            else:
                pass
        if s[0] + 1 != len(m) and found_path == False:
            new_s = (s[0] + 1, s[1])
            if m[new_s[0]][new_s[1]] != 'P':
                south = MazeSolver(m, new_s, g)
            else:
                pass
        if s[1] + 1 !=  len(m[0]) and found_path == False:
            new_e = (s[0], s[1]+1)
            if m[new_e[0]][new_e[1]] != 'P':
                east = MazeSolver(m, new_e, g)
            else:
                pass



        if east == False and south == False and west == False and north == False:
            m[s[0]][s[1]] = '0'
        return east or south or west or north




def print_maze(maze):
    for line in maze:
        print(line)

maze1_name = 'maze1.txt'
maze2_name = 'maze2.txt'
maze3_name = 'maze3.txt'
muhmaze_name = 'muhmaze.txt'

muhmaze = get_maze(muhmaze_name)


# print_maze(muhmaze)
# print('ya')
print(MazeSolver(muhmaze, (0, 0), (4, 7)))
# print_maze(muhmaze)
# print(maze1[s[0]][s[1]])
# print(maze1[s[0]][s[1]+1])
# print(s[1]+1)
# print(maze1[s[0]][s[1]+1])
