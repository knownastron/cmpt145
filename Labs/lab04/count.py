# count.py

def sum_to(x):
    '''
    Purpose:
        Calculate the sum of numbers 1 to x.
    Pre-conditions:
        x: a positive integer
    Post-conditions:
        none
    Return:
        an integer
    '''
    total = 0
    for i in range(x+1):
        total += i
    return total

print('Global code in count')
