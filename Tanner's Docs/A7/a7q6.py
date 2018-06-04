# CMPT 145: Recursion on Node-Based Data Structures
# 201801.A7.Q6


import node as node


def subst(anchor, t, r):
    """
    Purpose
        Replace every occurrence of t in the chain with the value r
    Preconditions:
        :param anchor: a node-chain
        :param t: the target value to be replaced
        :param r: the replacement value
    Post-conditions:
        Every occurrence of t is replaced by r
    Return:
        :return: None
    """

    if anchor is None:
        return
    else:
        data = node.get_data(anchor)
        if data == t:
            node.set_data(anchor,r)
        subst(node.get_next(anchor), t, r)

    

def reverse_b(to_reverse, reversed=None):
    """
    Purpose
        Move all of the nodes in to_reverse to reversed
    Preconditions:
        :param to_reverse: a node chain to be reversed
        :param reversed: a node chain already reversed
    Post-conditions:
        to_reverse is reversed
    Return:
        :return: the resulting node chain with all nodes
    """
    
    # "pop" off a node from q, push it on s
    if to_reverse == None:
        return reversed
    else:
    	# conceptually, grab the first node in to_reverse
        this_node = to_reverse
        # conceptually, grab the nodes after the first
        the_rest = node.get_next(this_node)
        # connect the first node to the ones that are already reversed
        node.set_next(this_node, reversed)
        # recursively reverse all the rest
        return reverse_b(the_rest, this_node)

def reverse_a(chain):
    """
    Purpose
        Reverse the sequence of the nodes in the given chain.
    Preconditions:
        :param chain: a node chain
    Post-conditions:
        The values in the chain are in the reversed order.
    Return:
        :return: the reversed node chain
    """

    if chain is None:
        return None
    elif node.get_next(chain) is None:
        return chain
    else:
        # remember the first two nodes
        first = chain
        second = node.get_next(chain)
        # reverse the chain starting at the second node
        reved = reverse_a(second)
        # second is now last!  hook the first node
        node.set_next(second, first)
        node.set_next(first, None)
        return reved

def reverse_c(chain):
    """
    Purpose
        Reverse the sequence of the nodes in the given chain.
    Preconditions:
        :param chain: a node chain
    Post-conditions:
        The values in the chain are in the reversed order.
    Return:
        :return: the reversed node chain
    """

    if chain is None:
        return None
    elif node.get_next(chain) is None:
        return chain
    else:
        # remember the first two nodes
        first = chain
        second = node.get_next(chain)
        # reverse the chain starting at the second node
        reved = reverse_c(second)
        walker = reved
        prev = None
        while walker is not None:
            prev = walker
            walker = node.get_next(walker)
        if prev is not None:
            node.set_next(prev, first)
            node.set_next(first, None)
        return reved



def copy(chain):
    """
    Purpose
        Make a completely new copy of the given node-chain.
    Preconditions:
        :param chain: a node-chain
    Post-conditions:
        None
    Return:
        :return: A new copy of the chain is returned
    """
    if chain == None:
        return None
    else:
        newnode = node.create(node.get_data(chain))
        newnext = copy(node.get_next(chain))
        node.set_next(newnode, newnext)
        return newnode



