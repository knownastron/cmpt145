# CMPT 145: Primitive Binary Search Trees
# Defines functions for primitive Binary Search Tree data structure
#
# A Primitive Binary Tree is defined as follows:
# 1. The value None is a primitive binary tree;
#    None is an empty tree.
# 2. If lt and rt are primitive binary trees, and d is any value
#    treenode.create(d, lt, rt) is a primitive binary tree.

# A Primitive Binary Tree t satisfies the Binary Search Tree property
# if all of the following hold:
# 1. The data value stored in t is greater than any data value in
#    t's left subtree (if any)
# 2. The data value stored in t is less than any data value in
#    t's right subtree (if any)
# 3. T's left subtree satisfies the BST property
# 4. T's right subtree satisfies the BST property

import treenode as tn

def member_prim(tnode, value):
    """
    Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a binary search tree
        :param value: a value
    Postconditions:
        none
    :return: True if value is in the tree
    """
    if tnode is None:
        return False
    else:
        cval = tn.get_data(tnode)
        if cval == value:
            # found the value
            return True
        elif value < cval:
            # use the BST property
            return member_prim(tn.get_left(tnode), value)
        else:
            return member_prim(tn.get_right(tnode), value)



def insert_prim(tnode,value):
    """
    Insert a new value into the binary tree.
    Preconditions:
        :param tnode: a binary search tree, created by create()
        :param value: a value
    Postconditions:
        If the value is not already in the tree, it is added to the tree
    Return
        :return: flag, tree
        Flag is True is insertion succeeded; tree is the tree with value in it
        Flag is False if the value is already in the tree, tree is returned unchanged
    """

    if tnode is None:
        return True, tn.create(value)
    else:
        cval = tn.get_data(tnode)
        if cval == value:
            return False, tnode
        elif value < cval:
            flag, subtree = insert_prim(tn.get_left(tnode), value)
            if flag:
                tn.set_left(tnode,subtree)
            return flag, tnode
        else:
            flag, subtree = insert_prim(tn.get_right(tnode), value)
            if flag:
                tn.set_right(tnode,subtree)
            return flag, tnode


def delete_prim(tnode, value):
    """
    Delete a value from the binary tree.
    Preconditions:
        :param tnode: a binary search tree, created by create()
        :param value: a value
    Postconditions:
        If the value is in the tree, it is deleted.
        If the value is not there, there is no change to the tree.
    Return:
        :return: (True, tnode) is the value was deleted, tree changed
                 (False, tnode) otherwise (tnode unchanged)
    """

    def delete_bst(tnode):
        if tnode is None:
            return False, tnode
        else:
            cval = tn.get_data(tnode)
            if cval == value:
                return reconnect(tnode)
            elif value < cval:
                flag, subtree = delete_bst(tn.get_left(tnode))
                if flag:
                    tn.set_left(tnode,subtree)
                return flag, tnode
            else:
                flag, subtree = delete_bst(tn.get_right(tnode))
                if flag:
                    tn.set_right(tnode,subtree)
                return flag, tnode

    def reconnect(delthis):
        if tn.get_left(delthis) is None \
                and tn.get_right(delthis) is None:
            # the deleted node has no children
            return True, None
        elif tn.get_left(delthis) == None:
            # the deleted node has one right child
            return True, tn.get_right(delthis)
        elif tn.get_right(delthis) == None:
            # the deleted node has one left child
            return True, tn.get_left(delthis)
        else:
            # the deleted node has 2 children
            left = tn.get_left(delthis)
            right = tn.get_right(delthis)
            walker = left
            # walk all the way to the right from left
            while tn.get_right(walker) != None:
                walker = tn.get_right(walker)
            tn.set_right(walker,right)
            return True, left

    flag, tree = delete_bst(tnode)

    return flag, tree


if __name__ == '__main__':

    def unit_member(atree, value, expected, reason):
        """
        Purpose: Test member_prim.
        Preconditions:
            :param atree: A primitive binary tree with the BST property
            :param value: A value to search for
            :param expected: The expected result of member_prim(atree,value)
            :param reason: A string about the reason for the test
        Return:
            :return: none
        """
        flag = member_prim(atree, value)
        if flag is not expected:
            print("Unit Test error: member_prim returned:", flag, reason)

    def unit_insert(atree, value, expected, reason):
        """
        Purpose: Test insert_prim.
        Preconditions:
            :param atree: A primitive binary tree with the BST property
            :param value: A value to insert into the tree
            :param expected: The expected result of insert_prim(atree,value)
            :param reason: A string about the reason for the test
        Return:
            :return: none
        """
        flag, result = insert_prim(atree, value)
        if flag is not expected:
            print("Unit Test error: insert_prim returned:", flag, reason)

    def unit_delete(atree, value, expected, reason):
        """
        Purpose: Test delete_prim.
        Preconditions:
            :param atree: A primitive binary tree with the BST property
            :param value: A value to delete
            :param expected: The expected result of delete_prim(atree,value)
            :param reason: A string about the reason for the test
        Return:
            :return: none
        """
        flag, result = delete_prim(atree, value)
        if flag is not expected:
            print("Unit Test error: delete_prim returned:", flag, reason)


    #################################################
    # unit test all functions

    # member
    unit_member(None, 1, False, 'on empty tree')
    unit_member(tn.create(1), 1, True, 'on one node tree containing data value')
    unit_member(tn.create(1), 2, False, 'on one node tree not containing data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)),  1, False, 'on three node tree without data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)),  7, False, 'on three node tree without data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)), 12, False, 'on three node tree without data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)), 17, False, 'on three node tree without data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)),  5, True,  'on three node tree containing data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)), 10, True,  'on three node tree containing data value')
    unit_member(tn.create(10, tn.create(5),tn.create(15)), 15, True,  'on three node tree containing data value')


    # insert
    unit_insert(None, 1, True, 'inserting into empty tree')
    unit_insert(tn.create(1), 1, False, 'on one node tree containing data value')
    unit_insert(tn.create(1), 0, True, 'on one node tree not containing data value (left insert)')
    unit_insert(tn.create(1), 2, True, 'on one node tree not containing data value (right insert)')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)),  7, True, 'inserting into three node tree without data')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)), 12, True, 'inserting into three node tree without data')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)), 17, True, 'inserting into three node tree without data')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)),  5, False, 'inserting into three node tree with data')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)), 10, False, 'inserting into three node tree with data')
    unit_insert(tn.create(10, tn.create(5), tn.create(15)), 15, False, 'inserting into three node tree with data')


    # delete
    unit_delete(None, 1, False, 'on empty tree')
    unit_delete(tn.create(1), 5, False, 'on tree without data value')
    unit_delete(tn.create(1), 1, True, 'on tree with data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)),  1, False, 'deleting from three node tree without data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)),  7, False, 'deleting from three node tree without data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)), 12, False, 'deleting from three node tree without data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)), 17, False, 'deleting from three node tree without data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)),  5, True, 'deleting from three node tree with data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)), 10, True, 'deleting from three node tree with data value')
    unit_delete(tn.create(10, tn.create(5), tn.create(15)), 15, True, 'deleting from three node tree with data value')



    def integration(unique, unknown, deleted, retained):
        """
        Purpose: To test the integration of member, insert, delete.
        Preconditions:
            :param unique: A list of unique values tio ubnsert into a tree
            :param unknown: A list of values not in the tree
            :param deleted:  A list of values to be deleted
            :param retained: A list of values that should still be in the tree at the end
        Return:
            :return: none
        """
        # start with an empty primitive tree
        atree = None

        # add all the unique values
        for v in unique:
            # first, the value should not already be in the tree
            fm = member_prim(atree, v)
            if fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'already in tree')

            # now the value gets inserted
            fi, atree = insert_prim(atree, v)
            if not fi:
                print("Integration Test error: insert_prim returned:", fi, 'unique value', v, 'already inserted')

            # after insert, the value should be there
            fm = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'inserted but not in tree')

        # check them all after all the insertions are done
        for v in unique:
            fm = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'inserted but not in tree')

        # check unknown values
        for v in unknown:
            # first check that member can't find it
            fm = member_prim(atree, v)
            if fm:
                print("Integration Test error: member_prim returned:", fm, 'unknown value', v, 'found in tree')

            # now check that delete can't delete it
            fd, atree = delete_prim(atree, v)
            if fd:
                print("Integration Test error: delete_prim returned:", fd, 'deleting unknown value', v)

        # delete a bunch of values that should be in the tree by now
        for v in deleted:
            # first check they are there
            fm = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'deleting value', v, 'not found in tree')

            # now delete it
            fd, atree = delete_prim(atree, v)
            if not fd:
                print("Integration Test error: delete_prim returned:", fd, 'deleting value', v, 'failed')

            # now check that member can't find it anymore
            fm = member_prim(atree, v)
            if fm:
                print("Integration Test error: member_prim returned:", fm, 'deleted value', v, 'found in tree')

        # last, check those that should be remaining
        for v in retained:
            fm = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'retained value', v, 'not in tree')


    # integration testing
    integration([1,2],[4],[1],[2])
    integration([1,2],[4],[1,2],[])
    integration([2,1,3],[4],[1,2,3],[])
    integration([10,5,15,3,6,9,12,17],[4,2,-1],[10,5,15,3,6,9,12,17],[])
    integration(sorted([10,5,15,3,6,9,12,17]),[4,2,-1],[10,5,15,3,6,9,12,17],[])
    integration([10,5,15,3,6,9,12,17],[4,2,-1],sorted([10,5,15,3,6,9,12,17]),[])
    integration(reversed([10,5,15,3,6,9,12,17]),[4,2,-1],[10,5,15,3,6,9,12,17],[])
    integration(reversed(sorted([10,5,15,3,6,9,12,17])),[4,2,-1],reversed([10,5,15,3,6,9,12,17]),[])

    import random as rand
    limit = 10000
    many = 1000
    first = many // 5
    second = 2 * first
    third = 3 * first
    fourth = 4 * first
    data = rand.sample(range(limit),many)

    integration(data[:third],data[third:fourth],data[first:second],data[:first])
    integration(sorted(data[:third]),data[third:fourth],data[first:second],data[:first])
    integration(data[:third],data[third:fourth],sorted(data[first:second]),data[:first])





