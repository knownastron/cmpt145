# CMPT 145: Binary trees
# Defines simple traversals for treenode (primitive) trees.
#
# These traversals print the data values stored in a primitive tree.

import treenode as tn

# not sure why, but my debugger doesn't like when I import Queue

import MyQueue as MyQueue


def in_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        in_order(tn.get_left(tnode))
        print(tn.get_data(tnode), end=" ")
        in_order(tn.get_right(tnode))


def pre_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        print(tn.get_data(tnode), end=" ")
        pre_order(tn.get_left(tnode))
        pre_order(tn.get_right(tnode))


def post_order(tnode):
    """
    Display the nodes of a tree in pre-order.
    :param tnode: a primitive tree
    :return: nothing
    """
    if tnode is None:
        return
    else:
        post_order(tn.get_left(tnode))
        post_order(tn.get_right(tnode))
        print(tn.get_data(tnode), end=" ")


def breadth_first_order(tnode):
    explore = MyQueue.create()
    MyQueue.enqueue(explore, tnode)

    while MyQueue.size(explore) > 0:
      current = MyQueue.dequeue(explore)
      print(tn.get_data(current), end=" ")
      left = tn.get_left(current)
      if left is not None:
          MyQueue.enqueue(explore, left)
      right = tn.get_right(current)
      if right is not None:
          MyQueue.enqueue(explore, right)


if __name__ == '__main__':
    # Create the tree we've been using in class
    root = tn.create(2)
    a =  tn.create(7)
    b =  tn.create(5)
    tn.set_left(root, a)
    tn.set_right(root, b)
    c =  tn.create(11)
    d =  tn.create(6)
    tn.set_left(a, c)
    tn.set_right(a, d)

    print("Pre-order traversal:", end=" ")
    pre_order(root)
    print()
    print("In-order traversal:", end=" ")
    in_order(root)
    print()
    print("Post-order traversal:", end=" ")
    post_order(root)
    print()
    print("Breadth-first order traversal:", end=" ")
    breadth_first_order(root)
    print()
