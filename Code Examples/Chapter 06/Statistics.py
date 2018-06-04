# CMPT 145: Abstract Data Types
# Defines the Statistics ADT
# Calculate mean and variance.

# Implementation
# Do the calculations without storing all the data!
# Uses a dictionary as a record to store three quantities:
#   'count':     the number of data values added
#   'avg':       the running average of the values added
#   'sumsqdiff': the sum of the square differences between the 
#                values added and the mean so far
# These values can be modified every time a new data value is 
# added, so that the mean and variance can be calculated quickly  
# as needed.  This approach means that we do not need to store  
# the data values themselves, which could save a lot of space.


def create():
    """
    Purpose:
        Create a Statistics record.
    Pre-conditions:
        (none)
    Post-conditions:
        a new record is allocated
    Return:
        A Statistics record.
    """
    b = {}
    b['count'] = 0      # how many data values have been seen
    b['avg'] = 0        # the running average so far
    b['sumsqdiff'] = 0  # the sum of the square differences
    return b


def add(stat, value):
    """
    Purpose:
        Use the given value in the calculation of statistics.
    Pre-Conditions:
        stat: a Statistics record
        value: the value to be added
    Post-Conditions:
        none
    Return:
        none
    """
    stat['count'] += 1
    k = stat['count']           # convenience
    diff = value - stat['avg']  # convenience
    stat['avg'] += diff/k
    stat['sumsqdiff'] += ((k-1)/k)*(diff**2)


def mean(stat):
    """
    Purpose:
        Return the mean of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The mean of the data seen so far.
        Note: if no data has been seen, 0 is returned.
              This is clearly false.
    """
    return stat['avg']


def var(stat):
    """
    Purpose:
        Return the variance of all the values seen so far.
        (variance is the average of the squared difference
        between each value and the average of all values)
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The variance of the data seen so far.
        Note: if 0 or 1 data values have been seen, 0 is returned.
              This is clearly false.
    """
    return stat['sumsqdiff']/stat['count']


def sampvar(stat):
    """
    Purpose:
        Return the sample variance of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The sample variance of the data seen so far.
        Note: if 0 or 1 data values have been seen, 0 is returned.
              This is clearly false.
    """
    return stat['sumsqdiff']/(stat['count'] - 1)



