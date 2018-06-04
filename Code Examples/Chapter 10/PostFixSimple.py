# CMPT 145: Linear ADTs
# Post-fix arithmetic evaluation

# An application of the Stack ADT
# and the Queue ADT

import Queue as Queue
import Stack as Stack


def evaluate(expr):
    """
    Evaluate a postfix expression.
    Pre-conditions:
       expr: a string containing a postfix expression
    Post-Conditions:
        none
    Return:
        the value of the expression
    """

    # create the initial empty data structures
    expression = Queue.create()
    evaluation = Stack.create()

    expr_list = expr.split()
    # put all the items in the Queue
    for c in expr_list:
        Queue.enqueue(expression, c)

    # evaluate the expression
    while not Queue.is_empty(expression):
        c = Queue.dequeue(expression)

        if c == '*':
            v1 = Stack.pop(evaluation)
            v2 = Stack.pop(evaluation)
            Stack.push(evaluation, v1*v2)
        elif c == '/':
            v1 = Stack.pop(evaluation)
            v2 = Stack.pop(evaluation)
            Stack.push(evaluation, v2/v1)
        elif c == '+':
            v1 = Stack.pop(evaluation)
            v2 = Stack.pop(evaluation)
            Stack.push(evaluation, v1+v2)
        elif c == '-':
            v1 = Stack.pop(evaluation)
            v2 = Stack.pop(evaluation)
            Stack.push(evaluation, v2-v1)
        else:
            Stack.push(evaluation, float(c))

    return Stack.pop(evaluation)


example = "f 56 + "
print('('+example+')', '=',evaluate(example))
