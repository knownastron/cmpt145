#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import sys
import TStack as Stack



def check_parentheses(expression):
    """
    Purpose:
        Takes in a string and checks that the string is balanced - every
        open parentheses, square bracket, or curly bracket has a corresponding
        closing one
    Pre-condition:
        :param expression: a string
    Post-condition:
        (none)
    Return: True if the expression is balanced
            False if the expression is not balanced
    """
    para_stack = Stack.create()

    for char in expression:
        #checks for opening parentheses
        if char == '(' or char == '[' or char == '{':
            Stack.push(para_stack, char)

        #checks for closing parentheses
        elif char == ')':
            if Stack.is_empty(para_stack) or Stack.peek(para_stack) != '(' :
                return False
            else:
                Stack.pop(para_stack)
        elif char == ']':
            if Stack.is_empty(para_stack) or Stack.peek(para_stack) != '[':
                return False
            else:
                Stack.pop(para_stack)
        elif char == '}':
            if Stack.is_empty(para_stack) or Stack.peek(para_stack) != '{':
                return False
            else:
                Stack.pop(para_stack)

    return (Stack.is_empty(para_stack))

if len(sys.argv) == 2:
    expression = sys.argv[1]
    result = check_parentheses(expression)
    if result == True:
        print("The expression is balanced")
    else:
        print("The expression is not balanced")
