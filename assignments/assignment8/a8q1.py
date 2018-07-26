#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import treenode as tn
import treefunctions as tf
import exampletrees as extree

def count_node_types(tnode, counter=(0,0)):
    """
    Purpose:
        Returns a tuple containing the number of leaf nodes in the tree,
        and the number of non-leaf nodes in the tree.
    """
    if tnode is None:
        return counter
    else:
        left = count_node_types(tn.get_left(tnode), counter)
        right = count_node_types(tn.get_right(tnode), counter)
        if tf.is_leaf(tnode):
            counter = (counter[0] + 1, counter[1])
        else:
            counter = (counter[0], counter[1] + 1)
        return (counter[0] + left[0] + right[0], counter[1] + left[1] + right[1])



def copy(tnode):
    """
    Purpose: To create an exact copy of the given tree, with completely new
    treenodes, but exactly the same data values, in exactly the same places
    """
    if tnode is None:
        return None
    else:
        cur_val = tn.get_data(tnode)
        new_tnode = tn.create(cur_val)
        tn.set_left(new_tnode, copy(tn.get_left(tnode)))
        tn.set_right(new_tnode, copy(tn.get_right(tnode)))
        return new_tnode

def collect_data_inorder(tnode):
    """
    Purpose: To collect all the data values in the given tree. Returns a list
    of all the data values, and the data values appear in the list according to
    the in-order sequence.
    """

    if tnode is None:
        return []
    else:
        return collect_data_inorder(tn.get_left(tnode)) + [tn.get_data(tnode)] \
               + collect_data_inorder(tn.get_right(tnode))

###############################################################################

my_tree = tn.create(10, tn.create(5), tn.create(15))

print(my_tree)
print('result', collect_data_inorder(my_tree))
