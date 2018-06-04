# CMPT 145: Assignment 4 Question 2
# Evaluating simple arithmetic expressions
#
# This implementation assumes expressions without any syntactic mistake.
# Clearly that's a bit too optimistic.

import TQueue as Queue
import TStack as Stack


def isfloat(str_val):
    """
    Purpose:
        Check whether a string represents a floating point str_val
    Pre-conditions
        str_val: a string
    Return: 
        True if str_val can be converted to a floating point number
    """
    try:
        float(str_val)
        # if it worked return True
        return True
    except:
        # didn't work, so False
        return False


def evaluate(expr):
    """
    Purpose:
        Evaluates an arithmetic expression.
    Precondition:
        expr: a string representation of an arithmetic expression
    Postcondition:
        none
    Returns:
        the numeric value of the expression if it's valid
    """

    symbols = Queue.create()
    for s in expr.split():
        Queue.enqueue(symbols, s)

    ops = Stack.create()
    vals = Stack.create()

    while not Queue.is_empty(symbols):
        s = Queue.dequeue(symbols)
        if isfloat(s):
            Stack.push(vals, float(s))
        elif s == '(':
            pass
        elif s == ')':
            op = Stack.pop(ops)
            v2 = Stack.pop(vals)
            v1 = Stack.pop(vals)
            if op == '+':
                result = v1 + v2
            elif op == '-':
                result = v1 - v2
            elif op == '*':
                result = v1 * v2
            elif op == '/':
                result = v1 / v2
            elif op == '%':
                result = v1 % v2
            else:
                print('unknown operator', op)
                return None
            Stack.push(vals,result)
        else:
            Stack.push(ops, s)

    return Stack.pop(vals)


