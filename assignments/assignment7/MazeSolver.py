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
        :param s: a tuple that represents the (x, y) coordinate of the starting
                  position
        :param g: a tuple that represents the (x, y) coordinate of the goal
                  position
    Post-condition:
        if a path is found from start to goal, the path taken will replace '0'
        with 'P'
    return:
        True if a path is found from s to g, false otherwise
    """
    val = m[s[0]][s[1]]
    if val == '0' and s == g:
        m[s[0]][s[1]] = 'P'
        #print the maze if g is reached
        print_maze(m)
        return True

    elif val == '1':
        return False

    else:
        east, south, west, north = False, False, False, False
        found_path = east or south or west or north

        m[s[0]][s[1]] = 'P'

        if s[0] != 0 and found_path == False: #check if path is already found
            new_n = (s[0] - 1, s[1]) #the new coordinates north of current location
            if m[new_n[0]][new_n[1]] != 'P': #check if new coordinates is already on the path
                north = MazeSolver(m, new_n, g)
            else:
                pass
        if s[1] != 0 and found_path == False: #check if path is already found
            new_w = (s[0], s[1]-1) #the new coordinates west of current location
            if m[new_w[0]][new_w[1]] != 'P': #check if new coordinates is already on the path
                west = MazeSolver(m, new_w, g)
            else:
                pass
        if s[0] + 1 != len(m) and found_path == False: #check if path is already found
            new_s = (s[0] + 1, s[1]) #the new coordinates south of current location
            if m[new_s[0]][new_s[1]] != 'P': #check if new coordinates is already on the path
                south = MazeSolver(m, new_s, g)
            else:
                pass
        if s[1] + 1 !=  len(m[0]) and found_path == False: #check if path is already found
            new_e = (s[0], s[1]+1) #the east coordinates west of current location
            if m[new_e[0]][new_e[1]] != 'P': #check if new coordinates is already on the path
                east = MazeSolver(m, new_e, g)
            else:
                pass


        #if current location does not on the way to g, set it back to '0'
        if east == False and south == False and west == False and north == False:
            m[s[0]][s[1]] = '0'
        return east or south or west or north


def print_maze(maze):
    """
    Purpose: prints out the input maze, each row on a seperate line
    Pre-conditions:
        :param maze: a list of lists where each element in the inner list is a '1'
                     or '0'
    return:
        None
    """
    for line in maze:
        print(line)

# if __name__ == '__main__':
#     print('Maze 1')
#     s, g = (0, 3), (4,5)
#     maze1 = get_maze('maze1.txt')
#     print(MazeSolver(maze1, s, g))
#
#     print('Maze 2')
#     s, g = (0,0), (8,9)
#     maze1 = get_maze('maze2.txt')
#     print(MazeSolver(maze1, s, g))
#
#     print('Maze 3')
#     s, g = (3,0), (23,30)
#     maze1 = get_maze('maze3.txt')
#     print(MazeSolver(maze1, s, g))
