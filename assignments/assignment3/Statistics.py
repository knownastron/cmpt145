#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

# CMPT 145: Abstract Data Types
# Defines the Statistics ADT
# Calculate mean and variance.

# Implementation
# Do the calculations without storing all the data!
# Uses a dictionary as a record to store three quantities:
#   'count':     the number of data values added
#   'avg':       the running average of the values added
#
# These values can be modified every time a new data value is
# added, so that the mean and variance can be calculated quickly
# as needed.  This approach means that we do not need to store
# the data values themselves, which could save a lot of space.

#####################################################################
# NOTE: This version of the Statistics ADT is simplified for
# Assignment 3: all calculations relevant to variance are removed.
# This makes the testing a little easier!
#####################################################################

def create():
    """
    Purpose:
        Create a Statistics record.
    Pre-conditions:
        (none)
    Post-conditions:
        a new record is allocated
    Return:
        A reference to a Statistics record.
    """
    b = {}
    b['count'] = 0      # how many data values have been seen
    b['avg'] = 0        # the running average so far
    b['max'] = None
    b['min'] = None
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

    #set max and/or min
    if stat['max'] == None and stat['min'] == None:
        stat['max'] = value
        stat['min'] = value
    elif value > stat['max']:
        stat['max'] = value
    elif value < stat['min']:
        stat['min'] = value


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
        Note: if no data has been seen, 0 is returned.
              This is clearly false.
    """
    return stat['count']

def minimum(stat):
    """
    Purpose:
        Return the minimum value of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The minimum value of the data seen so far.
        Note: if no data has been seen, None is returned.
              This is clearly false.
    """
    return stat['min']

def maximum(stat):
    """
    Purpose:
        Return the maximum value of all the values seen so far.
    Pre-conditions:
        stat: the Statistics record
    Post-conditions:
        (none)
    Return:
        The maximum value of the data seen so far.
        Note: if no data has been seen, None is returned.
              This is clearly false.
    """
    return stat['max']
