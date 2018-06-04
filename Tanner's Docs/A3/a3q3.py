# CMPT 145: ADTs
# Implement a simple ADT
#
# A Counter is a data structure to count things.
# For this task, we'll be counting immutable objects only
# (so numbers, strings, tuples, but not lists)
#
# Operations:
#    create()
#       Creates a data structure to record the number of times
#       (immutable) data values are seen.
#    see(counter, value)
#       Records the observation of the given value in the counter.
#    seen(counter, value)
#       Reports how often the given value in the counter was seen.
#    size(counter)
#       Reports how many different values the counter has seen.
#    total(counter)
#       Reports how many values the counter has seen in total.
#    unique(counter)
#       Returns the unique values seen by the counter.


def create():
    """
    Purpose:
        Create a data structure to store immutable data values.
    Return:
         A reference to a data structure.
    """
    # To-do: Replace this stub with something useful.
    b = {}
    b['counting'] = {}
    b['size'] = 0
    b['total'] = 0
    return b


def see(counter, value):
    """
    Purpose:
         Records the observation of the given value in the counter.
    Pre-conditions:
        :param counter: a reference to a counter data structure
        :param value: any immutable data value.
    Return:
        None
    """
    # To-do: Replace this stub with something useful.
    if value in counter['counting']:
        counter['counting'][value] += 1
    else:
        counter['counting'][value] = 1
        counter['size'] += 1
    counter['total'] += 1


def seen(counter, value):
    """
    Purpose:
         Reports how often the given value in the counter was seen.
    Pre-conditions:
        :param counter: a reference to a counter data structure
        :param value: any immutable data value.
    Return:
        The number of times the value was seen.
    """
    # To-do: Replace this stub with something useful.
    if value in counter['counting']:
        return counter['counting'][value]
    else:
        return 0


def size(counter):
    """
    Purpose:
         Reports how many different values the counter has seen.
    Pre-conditions:
        :param counter: a reference to a counter data structure
    Return:
        The number of unique values seen.
    """
    return counter['size']


def total(counter):
    """
    Purpose:
         Reports how many values the counter has seen in total.
    Pre-conditions:
        :param counter: a reference to a counter data structure
    Return:
        The total number of values seen.
    """
    return counter['total']

def unique(counter):
    """
    Purpose:
         Returns the unique values seen by the counter.
        :param counter: a reference to a counter data structure
    Return:
        A list containing all the unique values seen by the counter.
    """
    return [k for k in counter['counting']]

