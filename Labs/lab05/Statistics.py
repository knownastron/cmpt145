# CMPT 145: Abstract Data Types
# Defines the Statistics ADT
# Calculate mean and variance.

# Implementation
# Do the calculations without storing all the data!
# Use a Python dictionary as a record for storing three quantities:
#   'count':     the number of data values added
#   'avg':       the running average of the values added
#   'sumsqdiff': the sum of the square differences between the values added
#                and the mean so far
#   'min'
#   'max'
# These values can be modified every time a new data value is added, so that the
# mean and variance can be calculated quickly as needed.  This approach means that
# we do not need to store the data values themselves, which could save a lot of space.


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
    b['min'] = None
    b['max'] = None
    return b


def add(stat, value):
    """
    Purpose:
        Update the statistics with the given value.
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
    if stat['count'] == 1:
        stat['min'] = value
        stat['max'] = value
    else:
        stat['min'] = min(value,stat['min'])
        stat['max'] = max(value,stat['max'])


def mean(stat):
    """
    Purpose:
        Return the mean of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record containing the mean
    Post-conditions:
        (none)
    Return:
        The mean of the data seen so far.
        Note: if no data has been seen, 0 is returned.  This is clearly false.
    """
    return stat['avg']


def var(stat):
    """
    Purpose:
        Return the variance of all the values seen so far.
        (variance is the average of the squared difference between each value
        and the average of all values)
    Pre-conditions:
        stat: the Statistics record containing the variance
    Post-conditions:
        (none)
    Return:
        The variance of the data seen so far.
        Note: if 0 or 1 data values have been seen, 0 is returned.  This is clearly false.
    """
    return stat['sumsqdiff']/stat['count']


def sampvar(stat):
    """
    Purpose:
        Return the sample variance of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record containing the sample variance
    Post-conditions:
        (none)
    Return:
        The sample variance of the data seen so far.
        Note: if 0 or 1 data values have been seen, 0 is returned.  This is clearly false.
    """
    return stat['sumsqdiff']/(stat['count'] - 1)

def minimum(stat):
    """
    Purpose:
        Return the minimum of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The minimum of the data seen so far.
        Note: if no data has been seen, None is returned.
    """
    return stat['min']


def maximum(stat):
    """
    Purpose:
        Return the maximum of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The maximum of the data seen so far.
        Note: if no data has been seen, None is returned.
    """
    return stat['max']


def count(stat):
    """
    Purpose:
        Return the count of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The count of the data seen so far.
    """
    return stat['count']
    
    
def report(stat):
    """
    Purpose:
        Display a nicely formatted report on the statistics
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        Displays report on the console.
    Return:
        None
    """
    print('Average:', mean(stat), 'Minimum:', minimum(stat),
            'Maximum', maximum(stat), 'Variance:', var(stat), 
            'Size:', count(stat))
