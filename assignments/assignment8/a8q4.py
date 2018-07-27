#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03

import treenode as tn
import treefunctions as tf
import exampletrees as extree

def ordered(tnode):

    # helper internal function
    def collect_data_inorder(tnode):
        if tnode is None:
            return []
        else:
            return collect_data_inorder(tn.get_left(tnode)) + [tn.get_data(tnode)] \
                   + collect_data_inorder(tn.get_right(tnode))

    # main recursive procedure
    if tnode is None:
        return True
    else:
        cur_data = tn.get_data(tnode)
        left_sub = tn.get_left(tnode)
        right_sub = tn.get_right(tnode)
        left_list = collect_data_inorder(left_sub)
        right_list = collect_data_inorder(right_sub)

        if len(left_list) == 0 and len(right_list) == 0:
            return True
        elif len(left_list) == 0 and min(right_list) > cur_data:
            return ordered(right_sub)
        elif len(right_list) == 0 and max(left_list) < cur_data:
            return ordered(left_sub)
        if max(left_list) < cur_data and min(right_list) > cur_data:
            return ordered(left_sub) and ordered(right_sub)
        else:
            return False





###############################################################################
if __name__ == '__main__':
    expr_tree = extree.fibonatree
    fibTree = extree.fibonatree
    my_tree = tn.create(0,
                tn.create(0,
                    tn.create(0,
                        tn.create(0),
                        tn.create(0)),
                    tn.create(0,
                        tn.create(0),
                        tn.create(0))),
                tn.create(0,
                    tn.create(0,
                        tn.create(0),
                        tn.create(0)),
                    tn.create(0,
                        tn.create(0),
                        tn.create(0))))


    muh_tree = tn.create(10,
                    tn.create(5,
                        tn.create(1),
                        tn.create(7)),
                    tn.create(15,
                        tn.create(11),
                        tn.create(17)))

    muh_tree1 = tn.create(10)

    muh_tree2 = tn.create(10,
                    tn.create(5),
                    tn.create(3))
    print(tf.to_string(muh_tree))
    print(ordered(muh_tree))
