# CMPT 145: Binary trees
# Defines some helpful functions for trees
#

def is_leaf(tnode):
    """
    Purpose:
        Determine if tnode is a leaf.
    Pre-conditions:
        :param tnode: a treenode
    Return:
        True if the tnode has zero children
    """
    return TN.get_left(tnode) is None and TN.get_right(tnode) is None


def to_string(tnode, level=0):
    """
    Produce a formatted string to represent the hierarchy of
    a tree.  Tree diagrams usually have the root at the top.
    Here the root is at the top left.
    - every data value appears on its own line
    - the levels of a tree are columns from left to right
    - nodes at the same level start in the same column
    - very long data values might cause the presentation to get messy
    - subtrees appear below a parent
      - left subtree immediately
      - right subtree after the entire left subtree
    Pre-conditions:
        :param tnode: a Binary tree (treenode or None)
        :param level: the level of the tnode (default value 0)
    Return:
        A string with the hierarchy of the tree.
    """
    if tnode is None:
        return 'EMPTY'
    else:
        result = '\t'*level
        result += str(tn.get_data(tnode))
        if tn.get_left(tnode) is not None:
            result += '\n'+to_string(tn.get_left(tnode), level+1)
        if tn.get_right(tnode) is not None:
            result += '\n'+to_string(tn.get_right(tnode), level+1)
        return result
