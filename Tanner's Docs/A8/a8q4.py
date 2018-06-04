import treenode as tn

def ordered(tnode):
    """
    Purpose:
        Determine if the data values in the tree are ordered.
    Preconditions:
        :param tnode: a treenode
    Return
        :return: True if the data are ordered, False otherwise
    """
    def check(tree):
        """
        :param tree: a non-empty treenode
        :return: True, min, max, if ordered
                 False, None, None, if not ordered
        """
        # convenience!
        data = tn.get_data(tree)
        left = tn.get_left(tree)
        right = tn.get_right(tree)

        if left is None and right is None:
            return True, data, data
        elif left is None:
            # just look right
            flag, rmn, rmx = check(right)
            if flag and data < rmn:
                return True, data, rmx
            else:
                return False, None, None
        elif right is None:
            # just look left
            flag, lmn, lmx = check(left)
            if flag and data > lmx:
                return True, lmn, data
            else:
                return False, None, None
        else:
            # look right first
            rflag, rmn, rmx = check(right)
            if not rflag or data > rmn:
                return False, None, None
            # only look left if the right checks out
            lflag, lmn, lmx = check(left)
            if not lflag or data < lmx:
                return False, None, None
            # ordered!
            return True, lmn, rmx

    # body of ordered()
    if tnode is None:
        return True
    else:
        flag, _, _ = check(tnode)
        return flag

import math as math


tnc = tn.create
test_ordered = [
    {'inputs': None,
     'outputs': True,
     'reason': 'Empty tree'},

    {'inputs': tnc(4),
     'outputs': True,
     'reason': 'Singleton tree'},

    {'inputs': tnc(4, tnc(2)),
     'outputs': True,
     'reason': 'simple ordered tree with left only'},

    {'inputs': tnc(4, None, tnc(5)),
     'outputs': True,
     'reason': 'simple ordered tree with right only'},

    {'inputs': tnc(4, tnc(2), tnc(5)),
     'outputs': True,
     'reason': 'simple ordered tree with both children'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(6), tnc(10))),
     'outputs': True,
     'reason': 'three level tree, ordered and complete'},

    {'inputs': tnc(4, tnc(2, tnc(1), None), tnc(7, tnc(6), tnc(10))),
     'outputs': True,
     'reason': 'three level tree, ordered and not complete on left side'},

    {'inputs': tnc(4, tnc(2, None, tnc(3)), tnc(7, tnc(6), tnc(10))),
     'outputs': True,
     'reason': 'three level tree, ordered and not complete on left side'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, None, tnc(10))),
     'outputs': True,
     'reason': 'three level tree, ordered and not complete on right side'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(6), None)),
     'outputs': True,
     'reason': 'three level tree, ordered and not complete on right side'},

    {'inputs': tnc(4, tnc(5)),
     'outputs': False,
     'reason': 'simple tree, left child too big'},

    {'inputs': tnc(4, None, tnc(3)),
     'outputs': False,
     'reason': 'simple tree, right child too small'},

    {'inputs': tnc(4, tnc(2), tnc(3)),
     'outputs': False,
     'reason': 'simple tree, right child too small'},

    {'inputs': tnc(4, tnc(2, tnc(5), tnc(3)), tnc(7, tnc(6), tnc(10))),
     'outputs': False,
     'reason': 'three level tree, complete, unordered on left side'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(0)), tnc(7, tnc(6), tnc(10))),
     'outputs': False,
     'reason': 'three level tree, complete, unordered on left side'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(0), tnc(10))),
     'outputs': False,
     'reason': 'three level tree, complete, unordered on right side'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(6), tnc(3))),
     'outputs': False,
     'reason': 'three level tree, complete, unordered on right side'},

    {'inputs': tnc(4, tnc(2, tnc(5), tnc(3)), tnc(7, tnc(6), tnc(10))),
     'outputs': False,
     'reason': 'three level tree, complete, unordered two levels down'},

    {'inputs': tnc(4, tnc(2, None, tnc(0)), tnc(7, tnc(6), tnc(10))),
     'outputs': False,
     'reason': 'three level tree, not complete, unordered two levels down'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, tnc(0), None)),
     'outputs': False,
     'reason': 'three level tree, not complete, unordered two levels down'},

    {'inputs': tnc(4, tnc(2, tnc(1), tnc(3)), tnc(7, None, tnc(3))),
     'outputs': False,
     'reason': 'three level tree, not complete, unordered two levels down'},
]
for t in test_ordered:
    tree = t['inputs']
    expected = t['outputs']
    assert ordered(tree) is expected, t['reason']
