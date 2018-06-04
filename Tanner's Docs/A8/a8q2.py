# CMPT 145: Binary trees
# CMPT 145 201801 Assignment 8 Question 2

import treenode as tn

def mirrored(t1, t2):
    """
    Purpose:
        Determine if t1 and t2 are mirrored.
    Pre-conditions:
        :param t1: a treenode
        :param t2: a treenode
    Return:
        :return: True if they are mirrored, False otherwise
    """
    if t1 is None and t2 is None:
        return True
    elif t1 is None or t2 is None:
        return False
    else:
        return (tn.get_data(t1) == tn.get_data(t2)
                and mirrored(tn.get_left(t1), tn.get_right(t2))
                and mirrored(tn.get_right(t1), tn.get_left(t2)))
