#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import sys
import TStack as Stack



expression = sys.argv[1]

para_stack = Stack.create()

for char in expression:
    #checks for opening parentheses
    if char == '(' or char == '[' or char == '{':
        Stack.push(para_stack, char)

    #checks for closing parentheses
    elif char == ')':
        if Stack.is_empty(para_stack):
            continue
        elif Stack.peek(para_stack) == '(' :
            Stack.pop(para_stack)
    elif char == ']':
        if Stack.is_empty(para_stack):
            continue
        elif Stack.peek(para_stack) == '[' :
            Stack.pop(para_stack)
    elif char == '}':
        if Stack.is_empty(para_stack):
            continue
        elif Stack.peek(para_stack) == '{' :
            Stack.pop(para_stack)

print(Stack.is_empty(para_stack))
