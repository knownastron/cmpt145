# CMPT 145.201801 Assignment 4 Question 1
# Working with stacks

import sys as sys
import TStack as Stack

def print_rev_line(line):
    """
    Purpose:
        Print the words in line to the console in reverse order
    Precondition:
        line: a string
    Post-condition:
        Displays a line of words to the console
    Returns:
        None
    """

    line_stack = Stack.create()
    for word in line.split():
        Stack.push(line_stack, word)

    while not Stack.is_empty(line_stack):
        print(Stack.pop(line_stack), end=' ')  # no newline
    print() # newline at the end


if len(sys.argv) != 2:
    # give help when called improperly
    print('usage:', sys.argv[0], '<filename>')
else:
    infile = open(sys.argv[1])

    # push all lines into a stack
    lines = Stack.create()
    for line in infile:
        line = line.rstrip()
        Stack.push(lines, line)
    infile.close()

    # print the lines in reverse
    while not Stack.is_empty(lines):
        line = Stack.pop(lines)
        # print each line in reverse order
        print_rev_line(line)

