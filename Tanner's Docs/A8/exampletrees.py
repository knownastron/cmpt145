# CMPT 145: Binary trees
# Defines a few example trees

import treenode as tn


atree = tn.create(2)
a = tn.create(7)
b = tn.create(5)
tn.set_left(atree, a)
tn.set_right(atree, b)
c = tn.create(11)
d = tn.create(6)
tn.set_left(a, c)
tn.set_right(a, d)

# an empty tree with a bad pun: it's empty
mtree = None

# a tree with one node only.  Yes, a bad pun too.
ctree = tn.create('si')

# a larger more e-xtree-me tree
xtree = tn.create(5,
              tn.create(1,None,
                        tn.create(4,
                                  tn.create(3,tn.create(2,None,None),None),
                                  None)),
              tn.create(9,tn.create(8,tn.create(7,tn.create(6,None,None),None),None),
                          tn.create(1,tn.create(3,None,None),tn.create(3,None,None))))


# and you thought puns wouldn't get worse...
fibonatree = tn.create(5,tn.create(2,tn.create(1,None,None),
                                     tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None))),
                         tn.create(3,tn.create(1,tn.create(0,None,None),
                                                 tn.create(1,None,None)),
                                     tn.create(2,tn.create(1,None,None),
                                                 tn.create(1,tn.create(0,None,None),
                                                             tn.create(1,None,None)))))


# a tree with some meaning
expr_tree = tn.create('*',
                  tn.create('+',
                            tn.create('+',
                                      tn.create(2.0, None, None),
                                      tn.create(3.0, None, None)),
                            tn.create(3.0, None, None)),
                  tn.create('+',
                            tn.create(4.0, None, None),
                            tn.create('/',
                                      tn.create(2.0, None, None),
                                      tn.create('+',
                                                tn.create(89.0, None, None),
                                                tn.create(3.0, None, None)))))
