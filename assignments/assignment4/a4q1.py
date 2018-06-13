#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

# Assignment 4 Question 1

import sys
import TStack as Stack
import TQueue as Queue


def get_cases():
    """
    Purpose:
        reads the file from console input. Turns each line into a list, each
        element is a word on the line.
    Pre-conditions:
        (none)
    Post-conditions:
        (none)
    Return:
        A list of lists, each sublist is a line from the txt file, each element
        is a string of characters
    """
    cases = []

    file_name = sys.argv[1]
    file = open(file_name, "r")
    line = file.readline().rstrip().split()

    while line:
        cases.append(line)
        line = file.readline().rstrip().split()

    return cases


def set_urgency(cases):
    """
    Purpose:
        Reads each element in a list of a list and appends the case to either
        a stack or a queue
    Pre-conditions:
        :param cases: a list of lists, each element in the sublist is a string
    Post-conditions:
        (none)
    Return:
        A dictionary, each key is a month and each value is a list of two
        elements, a stack of urgent cases and a queue of non-urgent cases
    """
    #create dictionary to track each month:
    months = {}

    for index, line in enumerate(cases):
        non_urgent = Queue.create()
        urgent = Stack.create()

        for case in line:
            if case[:3] == 'URG-':
                Stack.push(urgent, case)
            else:
                Queue.enqueue(non_urgent, case)

        months['Month ' + str(index +1)] = [urgent, non_urgent]

    return months


def print_cases(months):
    """
    Purpose:
        Prints the urgent cases in a month in LIFO order then prints all the
        non urgent cases in a month in FIFO on a single line
    Pre-conditions:
        :param months: A dictionary, each key is a month and each value is a
                list of two elements, a stack of urgent cases and a queue of
                non-urgent cases
    Post-conditions:
        The stack of urgent cases and the queue of non-urgent cases are emptied
    Return:
        (none)
    """
    for group in months:
        cases_for_month = ''
        len_urgent = len(months[group][0][1])
        len_non_urgent = len(months[group][1][1])

        cases_for_month += str(group) + ': ' #adds the month to the string to be printed

        #adds all the urgent cases in LIFO order to the line
        for i in range(len_urgent):
            cases_for_month += str(Stack.pop(months[group][0])) + " "
        #adds all the non-urgent in FIFO order to the line
        for k in range(len_non_urgent):
            cases_for_month += Queue.dequeue(months[group][1]) + " "
        print(cases_for_month)

if len(sys.argv) == 2:
    cases = get_cases()
    months = set_urgency(cases)
    print_cases(months)
