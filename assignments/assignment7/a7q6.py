#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

import node as node

def average(node_chain, sum=0, count=0):
    """
    Purpose:
        returns the average of all the data in the node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty, only contains numbers as data
    Return:
        :return: The average of all the data in the node chain
    """
    if node_chain is None:
        if count == 0:
            return 0
        else:
            return sum/count
    else:
        value = node.get_data(node_chain)
        return average(node.get_next(node_chain), sum + value, count + 1)

def reverse_chain(node_chain, prev_node=None):
    """
    Purpose:
        Completely reverses the order of the given node_chain.
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    Post-conditions:
        The front of the node_chain is altered to be the back, with all nodes now pointing next the opposite direction.
    Return:
        :return: The resulting node chain that has had its order reversed
    """
    if node_chain is None:
        return prev_node
    else:
        next = node.get_next(node_chain)
        node.set_next(node_chain, prev_node)
        return reverse_chain(next, node_chain)


def copy(node_chain, new_chain=None, head=None):
    """
    Purpose:
        Create a new node-chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
    return:
        :return: a seperate distinct chain that has the same values as node-chain
    """

    if node_chain is None:
        node.set_next(new_chain, None)
        return head
    else:
        value = node.get_data(node_chain)
        if new_chain is None:
            new_chain = node.create(value, None)
            head = new_chain
            return copy(node.get_next(node_chain), new_chain, head)
        else:
            node.set_next(new_chain, node.create(value))
            print(new_chain)
            return copy(node.get_next(node_chain), node.get_next(new_chain), head)




if __name__ == '__main__':
    several_node = node.create(0)
    for i in range(1,5):
        several_node = node.create(i, several_node)

    print(node.to_string(several_node))
    print(node.to_string(copy(several_node)))
