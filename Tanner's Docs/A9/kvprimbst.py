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

import kvtreenode as tn

def member_prim(tnode, key):
    """
    Check if value is stored in the binary search tree.
    Preconditions:
        :param tnode: a binary search tree
        :param key: a key
    Postconditions:
        none
    Return
        :return: (True, val) if key is in the tree with associated value
                 (False, None) if key is not in the tree
    """
    if tnode is None:
        return False, None
    else:
        ckey = tn.get_key(tnode)
        if ckey == key:
            # found the value
            return True, tn.get_value(tnode)
        elif key < ckey:
            # use the BST property
            return member_prim(tn.get_left(tnode), key)
        else:
            return member_prim(tn.get_right(tnode), key)



def insert_prim(tnode, key, value):
    """
    Insert a new key into the binary tree.
    Preconditions:
        :param tnode: a binary search tree, created by create()
        :param key: a key
    Postconditions:
        If the key is not already in the tree, it is added to the tree
        If the key is  already in the tree, its current value is replaced by value
    Return
        :return: flag, tree
        Flag is True is insertion succeeded; tree is the tree with key in it
        Flag is False if the key is already in the tree, key's value is replaced
    """

    if tnode is None:
        return True, tn.create(key, value)
    else:
        ckey = tn.get_key(tnode)
        if ckey == key:
            tn.set_value(tnode, value)
            return False, tnode
        elif key < ckey:
            flag, subtree = insert_prim(tn.get_left(tnode), key, value)
            if flag:
                tn.set_left(tnode,subtree)
            return flag, tnode
        else:
            flag, subtree = insert_prim(tn.get_right(tnode), key, value)
            if flag:
                tn.set_right(tnode,subtree)
            return flag, tnode


def delete_prim(tnode, key):
    """
    Delete a key from the binary tree.
    Preconditions:
        :param tnode: a binary search tree, created by create()
        :param key: a key
    Postconditions:
        If the key is in the tree, it is deleted.
        If the key is not there, there is no change to the tree.
    Return:
        :return: (True, tnode) is the key was deleted, tree changed
                 (False, tnode) otherwise (tnode unchanged)
    """

    def delete_bst(tnode):
        if tnode is None:
            return False, tnode
        else:
            ckey = tn.get_key(tnode)
            if ckey == key:
                return reconnect(tnode)
            elif key < ckey:
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

    def unit_member(atree, key, expected, reason):
        """
        Purpose: Test member_prim.
        Preconditions:
            :param atree: A primitive binary tree with the BST property
            :param key: A key to search for
            :param expected: The expected result of member_prim(atree,key)
            :param reason: A string about the reason for the test
        Return:
            :return: none
        """
        result = member_prim(atree, key)
        if result != expected:
            print("Unit Test error: member_prim returned:", flag, reason)

    def unit_insert(atree, key, value, expected, reason):
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
        flag, result = insert_prim(atree, key, value)
        if flag != expected:
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
        if flag != expected:
            print("Unit Test error: delete_prim returned:", flag, reason)

    def small_tree():
        return tn.create(1, "one")
    def three_tree():
        return tn.create(10, "ten", tn.create(5, "five"),tn.create(15,"fifteen"))
    #################################################
    # unit test all functions

    # member
    unit_member(None, 1, (False, None), 'on empty tree')
    unit_member(small_tree(), 1, (True, "one"), 'on one node tree containing data value')
    unit_member(small_tree(), 2, (False, None), 'on one node tree not containing data value')
    unit_member(three_tree(),  7, (False, None), 'on three node tree without data value')
    unit_member(three_tree(), 12, (False, None), 'on three node tree without data value')
    unit_member(three_tree(), 17, (False, None), 'on three node tree without data value')
    unit_member(three_tree(),  5, (True, "five"),  'on three node tree containing data value')
    unit_member(three_tree(), 10, (True, "ten"),  'on three node tree containing data value')
    unit_member(three_tree(), 15, (True, "fifteen"),  'on three node tree containing data value')


    # insert
    unit_insert(None, 1, "one", True, 'inserting into empty tree')
    unit_insert(small_tree(), 1, "one-more", False, 'on one node tree containing data value')
    unit_insert(small_tree(), 0, "zero", True, 'on one node tree not containing data value (left insert)')
    unit_insert(small_tree(), 2, "two", True, 'on one node tree not containing data value (right insert)')
    unit_insert(three_tree(),  7, "seven", True, 'inserting into three node tree without data')
    unit_insert(three_tree(), 12, "twelve", True, 'inserting into three node tree without data')
    unit_insert(three_tree(), 17, "seventeen", True, 'inserting into three node tree without data')
    unit_insert(three_tree(),  5, "five-prime", False, 'inserting into three node tree with data')
    unit_insert(three_tree(), 10, "ten-prime", False, 'inserting into three node tree with data')
    unit_insert(three_tree(), 15, "fifteen-prime", False, 'inserting into three node tree with data')


    # delete
    unit_delete(None, 1, False, 'on empty tree')
    unit_delete(small_tree(), 5, False, 'on tree without data value')
    unit_delete(small_tree(), 1, True, 'on tree with data value')
    unit_delete(three_tree(),  1, False, 'deleting from three node tree without data value')
    unit_delete(three_tree(),  7, False, 'deleting from three node tree without data value')
    unit_delete(three_tree(), 12, False, 'deleting from three node tree without data value')
    unit_delete(three_tree(), 17, False, 'deleting from three node tree without data value')
    unit_delete(three_tree(),  5, True, 'deleting from three node tree with data value')
    unit_delete(three_tree(), 10, True, 'deleting from three node tree with data value')
    unit_delete(three_tree(), 15, True, 'deleting from three node tree with data value')



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
            fm, val = member_prim(atree, v)
            if fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'already in tree')

            # now the value gets inserted
            fi, atree = insert_prim(atree, v, "new-"+str(v))
            if not fi:
                print("Integration Test error: insert_prim returned:", fi, 'unique value', v, 'already inserted')

            # after insert, the value should be there
            fm, val = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'inserted but not in tree')

        # check them all after all the insertions are done
        for v in unique:
            fm, val = member_prim(atree, v)
            if not fm:
                print("Integration Test error: member_prim returned:", fm, 'unique value', v, 'inserted but not in tree')

        # check unknown values
        for v in unknown:
            # first check that member can't find it
            fm, val = member_prim(atree, v)
            if fm:
                print("Integration Test error: member_prim returned:", fm, 'unknown value', v, 'found in tree')

            # now check that delete can't delete it
            fd, atree = delete_prim(atree, v)
            if fd:
                print("Integration Test error: delete_prim returned:", fd, 'deleting unknown value', v)

        # delete a bunch of values that should be in the tree by now
        for v in deleted:
            # first check they are there
            fm, val = member_prim(atree, v)
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
            fm, val = member_prim(atree, v)
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





