#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03

import treenode as tn
import treefunctions as tf
import exampletrees as extree

def count_node_types(tnode):
    """
    Purpose:
        Returns a tuple containing the number of leaf nodes in the tree,
        and the number of non-leaf nodes in the tree.
    Pre-conditions:
        :param tnode: a treenode
    return: a tuple (number of leaf nodes, number of non-leaf nodes)
    """
    if tnode is None:
        return 0,0
    else:
        left = count_node_types(tn.get_left(tnode))
        right = count_node_types(tn.get_right(tnode))
        if tf.is_leaf(tnode):
            return (1 + left[0] + right[0], 0 + left[1] + right[1])
        else:
            return (0 + left[0] + right[0], 1 + left[1] + right[1])





def copy(tnode):
    """
    Purpose: To create an exact copy of the given tree, with completely new
        treenodes, but exactly the same data values, in exactly the same places
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        None
    return:
        A copy of tnode
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
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        None
    Return:
        a list of all the values in tnode in inorder sequence
    """

    if tnode is None:
        return []
    else:
        return collect_data_inorder(tn.get_left(tnode)) + [tn.get_data(tnode)] \
               + collect_data_inorder(tn.get_right(tnode))

def alter_subtrees(tnode, left_tree_offset, right_tree_offset, root_offset=0):
    """
    Purpose: Adds the given offsets to the data values of each subtree
             (and current root).
    Pre-conditions:
        :param tnode: a treenode
    Post-conditions:
        tnode is altered according to the offset arguments
    Return:
        the altered tnode
    """


    if tnode is None:
        return tnode
    else:
        cur_val = tn.get_data(tnode)
        tn.set_data(tnode, cur_val + root_offset)
        alter_subtrees(tn.get_left(tnode), left_tree_offset, right_tree_offset, root_offset + left_tree_offset)
        alter_subtrees(tn.get_right(tnode), left_tree_offset, right_tree_offset, root_offset + right_tree_offset)
        return tnode
