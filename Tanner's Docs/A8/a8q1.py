# CMPT 145: Binary trees
# CMPT 145 201801 Assignment 8 Question 1

import treenode as tn
import exampletrees as egtree

def subst(tnode, t, r):
    """
    Purpose:
        Replace every occurrence of data value t with r in the tree
    Pre-conditions:
        :param tnode: a treenode
        :param: t: a target value
        :param: r: a replacement value
    Post-conditions:
        Every occurrence of the target value is replaced
    Return
        :return: None
    """
    if tnode == None:
        return
    else:
        if tn.get_data(tnode) == t:
            tn.set_data(tnode, r)
        subst(tn.get_left(tnode), t, r)
        subst(tn.get_right(tnode), t, r)


def count_smaller(tnode, target):
    """
    Purpose:
        Count the number of times a target value appears in the tree
        rooted at tnode.
    Pre-conditions:
        :param tnode: a treenode
        :param target: a value
    Return:
        The number of times a value appears in the tree.
    """
    if tnode is None:
        return 0
    else:
        total = count_smaller(tn.get_left(tnode), target) \
              + count_smaller(tn.get_right(tnode), target)
        if tn.get_data(tnode) < target:
            return 1 + total
        else:
            return total


def copy(tnode):
    """
    Purpose:
        Make a copy of the tree rooted at the given tnode.
    Pre-conditions:
        :param tnode: A treenode
    Return:
        :return: A copy of the tree.
    """
    if tnode is None:
        return None
    else:
        return tn.create(tn.get_data(tnode),
                         copy(tn.get_left(tnode)),
                         copy(tn.get_right(tnode)))


def collect_data_inorder(tnode):
    """
    Purpose:
        Return a list of data values with inorder sequence.
    Pre-conditions:
        :param tnode: a treenode
    Return
        :return: A list of data values, with inorder sequence
    """
    if tnode is None:
        return []
    else:
        return (collect_data_inorder(tn.get_left(tnode))
                + [tn.get_data(tnode)]
                + collect_data_inorder(tn.get_right(tnode)))

eg = egtree.expr_tree
print(complete(eg) == bad_complete(eg))
eg_copy = copy(eg)
print(eg is eg_copy, eg == eg_copy)
print(collect_data_inorder(eg_copy))
print(collect_data_inorder(egtree.fibonatree))
print(count_smaller(egtree.fibonatree, 3))