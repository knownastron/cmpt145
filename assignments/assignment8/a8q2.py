#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03

import treenode as tn
import treefunctions as tf
import exampletrees as extree

def weigh_tree(root):
    """
    Purpose: Takes in a tree and returns a tuple with 3 values: the summed
             total of the left subtree, the data value of the root node, and
             the summed total of the right subtree.
    Pre-condition:
        :param root: a root of a treenode
    Post-conditions:
        None
    return: a tuple (sum of left sub-tree, value of root, sum of right sub-tree)
    """

    if root is None:
        return (0, 0, 0)
    else:
        cur_data = tn.get_data(root)
        left_sub = tn.get_left(root)
        right_sub = tn.get_right(root)
        sum_left = weigh_tree(left_sub)
        sum_right = weigh_tree(right_sub)

        return (sum_left[0] + sum_left[2] + sum_left[1],
                cur_data,
                sum_right[0] + sum_right[2] + sum_right[1])
