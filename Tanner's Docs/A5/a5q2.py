# CMPT 145: Assignment 5 Question 2

import node as node

def count_chain(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    if node_chain is None:
        return 0
    else:
        return 1 + count_chain(node.get_next(node_chain))



def copy_chain(node_chain):
    """
    Purpose:
        Make a new node chain with the same values as in node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly None
    Return:
        :return: A copy of node chain, with new nodes, but the same data.
    """
    # special case: empty node chain
    if node_chain is None:
        return None
    else:
        walker = node_chain

        # remember the first node
        result = node.create(node.get_data(walker))
        walker = node.get_next(walker)
        walker2 = result

        # walk along the first chain, making copies of each node
        while walker is not None:
            node.set_next(walker2, node.create(node.get_data(walker)))
            walker2 = node.get_next(walker2)
            walker = node.get_next(walker)

        # return the anchor to the copy
        return result


def replace(node_chain, target, value):
    """
    Purpose:
        Replace every occurrence of data target in node_chain with data value
        The chain's data may change, but the node structure will not.
    Pre-Conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a data value
        :param value: a data value
    Post-conditions:
        The node-chain is changed, by replacing target with value everywhere.
    Return:
        :return: None
    """
    walker = node_chain
    while walker is not None:
        if node.get_data(walker) == target:
            node.set_data(walker, value)
        walker = node.get_next(walker)


def count_chain_v2(node_chain):
    """
    Purpose:
        Counts the number of nodes in the node chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Return:
        :return: The number of nodes in the node chain.
    """
    walker = node_chain
    counter = 0
    while walker is not None:
        walker = node.get_next(walker)
        counter += 1
    return counter
