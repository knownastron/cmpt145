# CMPT 145 Assignment 2 Question 1
# Sudoku Checker Program

import sys as sys

def check(group):
    '''
    Purpose:
        Check that the group contains numbers 1-9 exactly once each
    Pre:
        :param group: a list of integers
    Post:
        None
    Return:
        True if the group has all 1-9, False otherwise
    '''
    # remove items from the legit list
    legit = [1,2,3,4,5,6,7,8,9]
    for v in group:
        if v in legit:
            legit.remove(v)
        else:
            return False
    # if there are any left over, some number didn't appear
    if len(legit) != 0:
        return False
    else:
        return True


def check_all(square):
    '''
    Purpose:
        Check that the square is a sudoku square
    Pre:
        :param square: a list of lists
    Post:
        None
    Return:
        True if square is a sudoku square
    '''

    # check each row
    for row in square:
        if not check(row):
            # broken row; don't need to check any more
            return False

    # check each column
    for c in range(9):
        col = [row[c] for row in square]
        if not check(col):
            # broken column; don't need to check any more
            return False

    # check each block
    # r,c identifies the left-corner of each block
    for r in range(0,9,3):
        for c in range(0,9,3):
            # now pull numbers from the 3x3 region
            block = []
            for br in range(3):
                for bc in range(3):
                    block.append(square[r+br][c+bc])
            if not check(block):
                # broken block; don't need to check any more
                return False

    return True

# main program
# only run if the right number of arguments are given.

if len(sys.argv) == 2:
    # open the file
    fname = sys.argv[1]
    file = open(fname)

    # create the list of lists
    square = []
    for i in range(9):
        line = file.readline()
        line = line.rstrip().split()
        row = [int(x) for x in line]
        square.append(row)

    # call check_all()
    if check_all(square):
        print('yes')
    else:
        print('no')

# end of a2q1.py
