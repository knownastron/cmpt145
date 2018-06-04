# CMPT 145: Linear ADTs
# Test the evaluator

import a4q2 as evaluator

# dictionary of test case suite to feed into test driver loop
test_suite = [

    {"inputs": ['( 3 + 4 )'],
     "outputs": 7,
     "reason": "addition"},

    {"inputs": ['( 4 + 3 )'],
     "outputs": 7,
     "reason": "addition"},

    {"inputs": ['( 3 * 4 )'],
     "outputs": 12,
     "reason": "multiplication"},

    {"inputs": ['( 4 * 3 )'],
     "outputs": 12,
     "reason": "multiplication"},

    {"inputs": ['( 12 / 3 )'],
     "outputs": 12.0/3.0,
     "reason": "division"},

    {"inputs": ['( 3 / 12 )'],
     "outputs": 3.0/12.0,
     "reason": "division"},

    {"inputs": ['( 12 - 4 )'],
     "outputs": 8,
     "reason": "subtraction"},

    {"inputs": ['( 4 - 12 )'],
     "outputs": -8,
     "reason": "subtraction"},

    {"inputs": ['( ( 3 * 4 ) + ( 5 * 6 ) )'],
     "outputs": 42,
     "reason": "order of operations"},

    {"inputs": ['( ( ( ( 1 + 2 ) + 3 ) + 4 ) + 5 )'],
     "outputs": 15,
     "reason": "sequence"},

    {"inputs": ['( -3 * 4 )'],
     "outputs": -12,
     "reason": "negatives"},

    {"inputs": ['( 3 * 4.2 )'],
     "outputs": 12.6,
     "reason": "fractions"},

    {"inputs": ['( -3 * +4.2 )'],
     "outputs": -12.6,
     "reason": "negatives and fractions"}
]

# run the tests
for test in test_suite:
    inputs = test["inputs"]
    result = evaluator.evaluate(inputs[0])
    if abs(result - test["outputs"]) > 0.001:
        print("Testing fault: evaluate() returned",result,
              "instead of", test["outputs"], "on inputs",inputs[0],
              "(",test["reason"],")")

print('*** test complete ***')
