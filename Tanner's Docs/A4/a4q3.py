# CMPT 145: Linear ADTs
# A read-Eval-Print Loop for the evaluator

import a4q2 as evaluator

while True:
    expr = input("> ")
    if expr == 'quit':
        exit()
    val = evaluator.evaluate(expr)
    print(val)
