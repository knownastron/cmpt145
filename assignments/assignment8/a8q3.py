#Name: Jason Tran
#NSID: jat687
#Student Number: 1101081
#Course: CMPT 145-01
#Lab: L03

import exampletrees as exampletrees
import treenode as tn
import treefunctions as tf

def cmplt(tnode):
    def int_cmplt(tnode):
        if tnode is None:
            return (True, 0)
        else:
            flag_left, ldepth = int_cmplt(tn.get_left(tnode))
            flag_right, rdepth = int_cmplt(tn.get_right(tnode))

            if ldepth == rdepth:
                return (flag_left and flag_right, rdepth + 1)
            else:
                return (False, 0)
    flag, height = int_cmplt(tnode)
    return flag


###############################################################################
if __name__ == '__main__':
    expr_tree = exampletrees.fibonatree
    fibTree = exampletrees.fibonatree
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

    muh_tree = tn.create(1, tn.create(3), tn.create(4))
    print(tf.to_string(muh_tree))
    print(cmplt(muh_tree))