# CMPT 145: Linear ADTs
# Application: Bracket Matching Algorithm
#
# Check a string for matching brackets
# Uses the Queue and Stack ADTs

import Queue as Queue
import Stack as Stack

example = '( ( ) ( ) ) )'

# create the initial empty containers
chars    = Queue.create()
brackets = Stack.create()
unmatched_close = False


# put all the characters in the Queue
for c in example:
    Queue.enqueue(chars, c)


# brackets match if and only if every '(' has
# a corresponding ')'
while not Queue.is_empty(chars) and not unmatched_close:
    c = Queue.dequeue(chars)
    if c == '(':
        Stack.push(brackets,c)
    elif c == ')' and not Stack.is_empty(brackets):
        Stack.pop(brackets)
    elif c == ')' and Stack.is_empty(brackets):
        unmatched_close = True
    else:
        pass


# check how the analysis turned out
if unmatched_close:
    print("Found a ')' with no matching '('")
elif not Stack.is_empty(brackets):
    print("At least one '(' without a matching ')'")
else:
    print('Brackets matched')

