# CMPT 145 - Algorithms
# The Maximum Slice Problem
# Given a list A containing (positive and negative) numbers,
# Find the slice A[a:b] that has the maximum sum

import random as rand
import time as time


# pedagogical example:
def allslices(alist):
    """
    Purpose:
        Display all slices to the console.
    Preconditions:
        alist: a list of numbers
    Post-conditions:
        Outputs all slices to the console.
    Return:
        None
    """
    for a in range(len(alist)):
        for b in range(a,len(alist)):
            print(alist[a:b+1])


# version 0: naively sums each slice
def maxslice_brute_force_v0(alist):
    """
    Purpose:
        Find the maximum sum of all slices of alist.
    Preconditions:
        alist: a list of numbers
    Post-conditions:
        None
    Return:
        a number, the maximum slice sum
    """
    maxsum = alist[0]
    for i in range(len(alist)):
        for j in range(i+1, len(alist)):
            slice = sum(alist[i:j + 1])
            if slice > maxsum:
                maxsum = slice
    return maxsum


# version 1: sums the slices more cleverly
def maxslice_brute_force_v1(alist):
    """
    Purpose:
        Find the maximum sum of all slices of alist.
    Preconditions:
        alist: a list of numbers
    Post-conditions:
        None
    Return:
        a number, the maximum slice sum
    """
    # using brute force: look at all possible slices
    # but store all the partial sums in a dictionary
    # where s[j] stores the value sum(alist[i,j+1])

    maxsum = alist[0]
    for i in range(len(alist)):
        s = {}
        s[i] = alist[i]
        if s[i] > maxsum: 
            maxsum = s[i]
        for j in range(i+1, len(alist)):
            s[ j] = s[j-1] + alist[j]
            if s[j] > maxsum: 
                maxsum = s[j]
    return maxsum


# version 2 uses divide and conquer
# Divide the list into 2 halves
# The maximum slice can occur in one of 3 ways:
# 1. Starts and finishes on the left half
# 2. Starts and finishes on the right half
# 3. Starts somewhere in the left half, and
#    continues somewhere to the right half
def maxslice_DC(alist):
    """
    Purpose:
        Find the maximum sum of all slices of alist.
    Preconditions:
        alist: a list of numbers
    Post-conditions:
        None
    Return:
        a number, the maximum slice sum
    """

    # internal function
    def max_tail(left, right):
        """
        Calculate the maximum slice that ends at right
        (from any point starting at left or later)
        """
        s = {}
        s[right] = alist[right]
        maxsum = s[right]
        # calculate the sums from right to left (backwards)
        for i in range(right - 1, left - 1, -1):
            s[i] = s[i + 1] + alist[i]
            if s[i] > maxsum: 
                maxsum = s[i]
        return maxsum

    # internal function
    def max_head(left, right):
        """
        Calculate the maximum slice that starts at left
        (to any point up to and including right)
        """
        s = {}
        s[left] = alist[left]
        maxsum = s[left]
        for i in range(left + 1, right + 1):
            s[i] = s[i - 1] + alist[i]
            if s[i] > maxsum: 
                maxsum = s[i]
        return maxsum

    # internal function
    def maxslice_rec(left, right):
        """
        Recursively find maximum slice between left and right.
        """
        # using divide and conquer
        if left == right:
            return alist[left]
        else:
            # divide, and solve
            mid = (right + left) // 2
            max_left  = maxslice_rec(left, mid)
            max_right = maxslice_rec(mid + 1, right)
            max_cross = (max_tail(left, mid) 
                         + max_head(mid + 1, right))
            # conquer
            return max(max_left, max_right, max_cross)

    # body of maxslice_DC
    return maxslice_rec(0, len(alist) - 1)


def allslices(alist):
    for a in range(len(alist)):
        for b in range(a,len(alist)):
            print(alist[a:b+1])

allslices([1,2,3,4])


# put the versions through their paces
if __name__ == '__main__':
    examples = [[1, 2, 3, 4, 5],
                [5, 4, -3, 2, 1],
                [1, 2, -3, 4, 5],
                [1, -2, 3, 4, -5],
                [1, -2, 3, 4, -5, 1, 2, 3, 4, 5, -6, -7, -8],
                [rand.randint(-100, 100) for i in range(1000)],
                [rand.randint(-100, 100) for i in range(2000)]
               ]

    for ex in examples:
        print('Example: list of length:', len(ex))

        print('Brute Force version 0:')
        start = time.process_time()
        result = maxslice_brute_force_v0(ex)
        end = time.process_time()
        print('Result:', result, 'Time:', (end - start))

        print('Brute Force version 1:')
        start = time.process_time()
        result = maxslice_brute_force_v1(ex)
        end = time.process_time()
        print('Result:', result, 'Time:', (end - start))

        print('Divide and conquer:')
        start = time.process_time()
        result = maxslice_DC(ex)
        end = time.process_time()
        print('Result:', result, 'Time:', (end - start))

        print()