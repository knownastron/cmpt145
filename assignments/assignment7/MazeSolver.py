#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

def get_maze(maze_name):
    maze = []
    lines_list = open(maze_name).read().splitlines()
    for line in lines_list:
        maze.append(line.split())
    return maze

def MazeSolver(m, s, g):
    val = m[s[0]][s[1]]
    if val == '0' and s == g:
        m[s[0]][s[1]] = 'P'
        return True
    elif val == '1':
        return False
    else:
        east, south, west, north = False, False, False, False

        m[s[0]][s[1]] = 'P'
        if s[0] != 0:
            new_n = (s[0] - 1, s[1])
            if m[new_n[0]][new_n[1]] != 'P':
                north = MazeSolver(m, new_n, g)
            else:
                pass
        if s[0] + 1 != len(m):
            new_s = (s[0] + 1, s[1])
            if m[new_s[0]][new_s[1]] != 'P':
                south = MazeSolver(m, new_s, g)
            else:
                pass
        if s[1] + 1 !=  len(m[0]):
            new_e = (s[0], s[1]+1)
            if m[new_e[0]][new_e[1]] != 'P':
                east = MazeSolver(m, new_e, g)
            else:
                pass
        if s[1] != 0:
            new_w = (s[0], s[1]-1)
            if m[new_w[0]][new_w[1]] != 'P':
                west = MazeSolver(m, new_w, g)
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

muhmaze = get_maze(maze3_name)


print_maze(muhmaze)
print(MazeSolver(muhmaze, (3,0), (23,30)))
print_maze(muhmaze)
# print(maze1[s[0]][s[1]])
# print(maze1[s[0]][s[1]+1])
# print(s[1]+1)
# print(maze1[s[0]][s[1]+1])
