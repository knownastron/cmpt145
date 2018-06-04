# CMPT 145 - Algorithms
# The Leap Line Problem
# Given a list A containing (positive and negative) numbers,
# Assuming a collection policy
# Find the maximum score that can be collected
#
# Collection policy:
#   Mario must leap over 1 item or step into it
#   Leaping over item prevents collection
#   Stepping into an item ensures collection

import time as time


# The collection policy.
# Change the return value for leaps!
def collection(action):
    """
    Isolate the collection policy for easy modification!
    :param action: a string, either 'step' or 'leap'
    :param loc: the current position
    :return: a new position
    """
    if action == 'step':
        return 1
    elif action == 'leap':
        return 3
    else:
        raise Exception('Invalid action for collection policy')


# version 0: Brute force
def maximumScoreFrom_v0(track):
    """
    Purpose:
        Calculate the maximum score that can be obtained from
        stepping and jumping along the given track
    Pre-conditions:
        :param track: a list of integers
    Return: 
        the maximum score
    """

    def jump_or_step(loc):
        """
        Calculate the maximum score that can be obtained from
        starting at the given location
        """
        step_loc = loc + 1
        jump_loc = loc + 2

        if step_loc == len(track):
            return track[loc]
        elif jump_loc >= len(track):
            return track[loc] + jump_or_step(step_loc)
        else:
            return track[loc] + max(jump_or_step(step_loc),
                                    jump_or_step(jump_loc))

    return jump_or_step(0)


# version 1: Using Memoization
def maximumScoreFrom_v1(track):
    """
    Purpose:
        Calculate the maximum score that can be obtained from
        stepping and jumping along the given track
    Pre-conditions:
        :param track: a list of integers
    Return: 
        the maximum score
    """
    def jump_or_step(loc):
        """
        Calculate the maximum score that can be obtained from
        stepping and jumping along the given track, starting
        at the given location
        """
        # check if the best score is already known
        if loc in memo:
            return memo[loc]

        step_loc = loc + 1
        jump_loc = loc + 2

        if step_loc == len(track):
            return track[loc]
        elif jump_loc >= len(track):
            result = track[loc] + jump_or_step(step_loc)
            memo[loc] = result
            return result
        else:
            result = track[loc] + max(jump_or_step(step_loc),
                                      jump_or_step(jump_loc))
            memo[loc] = result
            return result
            
    # body of maximumScoreFrom_v1()
    # using memoization
    # memo[loc] stores the best score starting from loc.
    memo = {}
    return jump_or_step(0)


# version 2: Greedy
# looks one location ahead, and leaps over -1
def maximumScoreFrom_v2(track):
    """
    Calculate the maximum score that can be obtained from
    stepping and leaping along the given track
    :param track: a list of integers
    :return: the maximum score
    """

    def leap_or_step(loc):
        """
        Calculate the maximum score that can be obtained from
        stepping and leaping along the given track, starting
        at the given location
        """
        step_loc = loc + 1
        leap_loc = loc + 2

        if step_loc == len(track):
            return track[loc]
        elif leap_loc >= len(track):
            return track[loc] + leap_or_step(step_loc)
        elif track[step_loc] < 0:
            # greedy choice: avoid negatives
            return track[loc] + leap_or_step(leap_loc)
        else:
            # greedy choice: collect 1
            return track[loc] + leap_or_step(step_loc)

    return leap_or_step(0)


examples = [
    ['easy',
       [0, -1, -1, 1, -1, -1, 0]],
    ['medium',
       [0, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 0]],
    ['challenging',
       [0, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 0]],
    ['hardmode',
       [0, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1,
        1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1,
        -1, 1, -1, -1, 1, 1, 1, -1, 0]],
    ['very_hard',
       [0, -1, 1, -1, -1, 1, -1, -1, 1, -1, 1, -1, -1, 1,
        1, 1, -1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1,
        1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1,
        1, -1, -1, 0]]
]

for e in examples:
    print('Example: list of length:', len(e[1]))

    print('Brute Force version (v0):', end=" ")
    start = time.process_time()
    result = maximumScoreFrom_v0(e[1])
    end = time.process_time()
    print('Result', '(' + e[0] + '):', result,
          'Time:', (end - start))

    print('Memoized version (v1):', end=" ")
    start = time.process_time()
    result = maximumScoreFrom_v1(e[1])
    end = time.process_time()
    print('Result', '(' + e[0] + '):', result,
          'Time:', (end - start))

    print('Greedy version (v2):', end=" ")
    start = time.process_time()
    result = maximumScoreFrom_v2(e[1])
    end = time.process_time()
    print('Result', '(' + e[0] + '):', result,
          'Time:', (end - start))

    print()

