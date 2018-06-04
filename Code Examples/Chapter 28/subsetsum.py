# CMPT 145 - Algorithms
# The Subset Sum problem
#
# Given a list of integers L, and a target T
# Find a subset of numbers from L whose sum is T


# pedagogical example, working through subsets
def all_subsets(alist):
    """
    Purpose:
        Given a list, display all subsets.
    Preconditions:
        alist: a list
    Post-conditions:
        displays all subsets to the console, 
        one subset per line.  Could be a lot!
    Return:
        None
    """
    def allsub(al, sub):
        if len(al) == 0:
            print(sub)
        else:
            first = al[0] 
            rest = al[1:]
            allsub(rest, [first]+sub)  # with first
            allsub(rest, sub)          # without first
    
    allsub(alist,[])


# Brute force solution
def subsetsum_v1(alist, target):
    """
    Purpose:
        Given a list of positive integers, and a target,
        Return a sublist of integers whose sum is target.
    Preconditions:
        alist: a list of positive integers
        target: a positive integer
    Return:
        A tuple True, sublist if sum(sublist) == target
        Or False, None otherwise
    """

    def trysum(al, subset):
        """
        Recursively try every subset of values from alist.
        """
        if len(al) == 0 and sum(subset) == target:
            return True, subset
        elif len(al) == 0:
            return False, None
        else:
            first = al[0]
            rest = al[1:]
            flag, answer = trysum(rest, subset + [first])
            if flag:
                return flag, answer
            else:
                # try without the first value
                return trysum(rest, subset)

    return trysum(alist, [])


# Backtracking solution
def subsetsum_v2(alist, target):
    """
    Purpose:
        Given a list of positive integers, and a target,
        Return a sublist of integers whose sum is target.
    Preconditions:
        alist: a list of positive integers
        target: a positive integer
    Return:
        A tuple True, sublist if sum(sublist) == target
        Or False, None otherwise
    """

    def trysum(al, subset):
        """
        Recursively try every subset of values from alist.
        """
        if sum(subset) == target:
            return True, subset
        elif len(al) == 0 or sum(subset) > target:
            return False, None
        else:
            first = al[0]
            rest = al[1:]
            flag, answer = trysum(rest, subset + [first])
            if flag:
                return flag, answer
            else:
                # try without the first value
                return trysum(rest, subset)

    return trysum(alist, [])


# Backtracking solution
def subsetsum_v22(alist, target):
    """
    Purpose:
        Given a list of positive integers, and a target,
        Return a sublist of integers whose sum is target.
    Preconditions:
        alist: a list of positive integers
        target: a positive integer
    Return:
        A tuple True, sublist if sum(sublist) == target
        Or False, None otherwise
    """

    def trysum(al, subset, thesum):
        """
        Recursively try every subset of values from alist.
        """
        if thesum == target:
            return True, subset
        elif len(al) == 0 or thesum > target:
            return False, None
        else:
            first = al[0]
            rest = [v for v in al[1:] if v <= (target - thesum)]
            flag, answer = trysum(rest, subset + [first], thesum+first)
            if flag:
                return flag, answer
            else:
                # try without the first value
                return trysum(rest, subset, thesum)

    return trysum(sorted(alist, reverse=True), [], 0)




# Divide and Conquer solution, not very smart
def subsetsum_v3(alist, target):
    """
    Purpose:
        Given a list, display all subsets.
    Preconditions:
        alist: a list
    Post-conditions:
        displays all subsets to the console, 
        one subset per line.  Could be a lot!
    Return:
        None
    """

    def trysum(alist, subset):
        """
        Recursively construct a subset from alist, checking
        if the sum is equal to the target.
        """
        if sum(subset) == target:
            return True, subset
        elif len(alist) == 0:
            return False, None
        else:
            tryit = alist[0]
            # try to find a subset sum using the first value
            flag, answer = trysum(alist[1:], subset + [tryit])
            if flag:
                return flag, answer
            else:
                # try without the first value
                return trysum(alist[1:], subset)

    # this does divide and conquer, in the form of
    # dividing the list in half
    def binary(alist):
        if len(alist) < 5:
            # for small lists, just use brute force!
            return trysum(alist, [])
        else:
            mid = len(alist)//2

            # try to find a solution in a list half the size
            flag, ans = binary(alist[:mid])
            if flag: return True, ans

            # if not, try the other half
            flag, ans = binary(alist[mid + 1:])
            if flag: return True, ans

            # if not, try the whole list
            return trysum(alist, [])

    return binary(alist)




import random as rand
import time as time
if __name__ == '__main__':

    example1 = [1, 2, 3, 4, 5]
    example2 = [1, 3, 5, 7]
    target = 8

    for ex in [example1, example2]:
        print('Example: list of length:', len(ex))

        print('Brute Force (Version 1):')
        start = time.process_time()
        subset = subsetsum_v1(ex, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print('Backtracking (Version 2):')
        start = time.process_time()
        subset = subsetsum_v2(ex, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print('Divide and Conquer (Version 3):')
        start = time.process_time()
        subset = subsetsum_v3(ex, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print()

    lo = 0
    hi = 5000
    example_size = 22
    example3 = [rand.randint(lo, hi)
                for i in range(example_size)]

    number_of_trials = 5
    for i in range(number_of_trials):
        target = rand.randint(hi, hi*100)

        print('Brute Force (Version 1) on list of size',
              example_size, ':')
        start = time.process_time()
        subset = subsetsum_v1(example3, target)
        #subset = None
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print('Backtracking (Version 2) on list of size',
              example_size, ':')
        start = time.process_time()
        subset = subsetsum_v2(example3, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print('Backtracking (Version 2.2) on list of size',
              example_size, ':')
        start = time.process_time()
        subset = subsetsum_v22(example3, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)
              
        print('Divide and Conquer (Version 3) on list of size',
              example_size, ':')
        start = time.process_time()
        subset = subsetsum_v3(example3, target)
        end = time.process_time()
        print('Target:', target,
              'Time:', end - start,
              'Result:', subset)

        print()