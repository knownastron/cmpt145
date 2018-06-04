# CMPT 145:  Binary Search Trees
#       Implements the Table ADT
#
# Data structure:
#   a table is a dictionary containing two keys:
#     'root'  - value stores the root of a primitive binary tree
#     'size'  - value stores the number of nodes in the primitive binary tree
# The operations should ensure that the primitive binary tree satisfies the
# binary search tree property
#
# The primitive binary tree is built using key-value treenodes

import kvprimbst as primbst
import kvtreenode as tn

def create():
    """
    Purpose:
        Create a new table.
    Return:
        :return: a new empty table
    """
    table = {}
    table['root'] = None
    table['size'] = 0

    return table


def size(atable):
    """
    Purpose:
        Return the size of the given table.
    Preconditions:
        :param atable: a table created by create()
    Return:
        :return: the number of key,value pairs in the table
    """
    return atable['size']



def is_empty(atable):
    """
    Purpose:
        Indicate whether the given table is empty.
    Preconditions:
        :param atable: a table created by create()
    Return:
        :return: True if the table is empty
    """
    return atable['size'] == 0


def retrieve(atable, key):
    """
    Return the value associated with the given key.
    Preconditions:
        :param atable: a table, created by create()
        :param key: a key
    Postconditions:
        none
    Return
        :return: True, value if the key appears in the table
    """

    return primbst.member_prim(atable['root'], key)



def insert(atable, key, value):
    """
    Insert a new key, value into the table.
    Preconditions:
        :param atable: atable, created by create()
        :param key: a unique key for the value
        :param value: a value
    Postconditions:
        If the key is not already in the table, it is added to the table
        If the key is already there, change the value
    Return
        :return: True if the key,value was inserted
                 False if the value of an existing key was changed
    """

    flag, ptree = primbst.insert_prim(atable['root'], key, value)
    if flag:
        atable['root'] = ptree
        atable['size'] += 1
    return flag



def delete(atable, key):
    """
    Delete a given key and its associated value from the table.
    Preconditions:
        :param atable: atable, created by create()
        :param key: a unique key for the value
    Postconditions:
        If the key is not in the table, no change to the table
        If the key is in the table, remove it
    Return
        :return: True if the key,value was deleted
    """

    flag, tree = primbst.delete_prim(atable['root'], key)
    if flag:
        atable['root'] = tree
        atable['size'] -= 1
    return flag


if __name__ == '__main__':

    def int_key_to_v(k):
        return "val-"+str(k)

    def integration(unique, unknown, deleted, retained):
        """
        Purpose: To test the integration of member, insert, delete.
        Preconditions:
            :param unique: A list of unique values to into a table
            :param unknown: A list of values not in the table
            :param deleted:  A list of values to be deleted
            :param retained: A list of values that should still be in the tree at the end
        Return:
            :return: none
        """
        # start with an empty primitive tree
        atable = create()

        # add all the unique values
        for key in unique:
            # first, the value should not already be in the tree
            fm, v = retrieve(atable, key)
            if fm:
                print("Integration Test error: retrieve returned:", fm, v, 'unique value', key, 'already in tree')

            # now the value gets inserted
            fi = insert(atable, key, int_key_to_v(key))
            if not fi:
                print("Integration Test error: insert returned:", fi, 'unique value', key, 'already inserted')

            # after insert, the value should be there
            fm, v = retrieve(atable, key)
            if not fm or v != int_key_to_v(key):
                print("Integration Test error: retrieve returned:", fm, v, 'unique value', key, 'inserted but not in tree')

        # check them all after all the insertions are done
        for key in unique:
            fm, v = retrieve(atable, key)
            if not fm:
                print("Integration Test error: retrieve returned:", fm, 'unique value', key, 'inserted but not in tree')

        # check unknown values
        for key in unknown:
            # first check that member can't find it
            fm, v = retrieve(atable, key)
            if fm:
                print("Integration Test error: retrieve returned:", fm, 'unknown value', key, 'found in tree')

            # now check that delete can't delete it
            fd = delete(atable, key)
            if fd:
                print("Integration Test error: delete returned:", fd, 'deleting unknown value', key)

        # delete a bunch of values that should be in the tree by now
        for key in deleted:
            # first check they are there
            fm, v = retrieve(atable, key)
            if not fm:
                print("Integration Test error: retrieve returned:", fm, 'deleting value', key, 'not found in tree')

            # now delete it
            fd = delete(atable, key)
            if not fd:
                print("Integration Test error: delete returned:", fd, 'deleting value', key, 'failed')

            # now check that member can't find it anymore
            fm, v = retrieve(atable, key)
            if fm:
                print("Integration Test error: retrieve returned:", fm, 'deleted value', key, 'found in tree')

        # last, check those that should be remaining
        for key in retained:
            fm, v = retrieve(atable, key)
            if not fm:
                print("Integration Test error: retrieve returned:", fm, 'retained value', key, 'not in tree')

            # change their values
            fm = insert(atable, key, int_key_to_v(key)+"-prime")
            if fm:
                print("Integration Test error: insert returned:", fm, 'retained value', key, 'did not get a new value')

            fm, v = retrieve(atable, key)
            if not fm or v != int_key_to_v(key)+"-prime":
                print("Integration Test error: retrieve returned:", fm, v, 'retained value', key, 'new value not found')


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
    many = 30
    first = many // 5
    second = 2 * first
    third = 3 * first
    fourth = 4 * first
    data = rand.sample(range(limit),many)

    integration(data[:third],data[third:fourth],data[first:second],data[:first])
    integration(sorted(data[:third]),data[third:fourth],data[first:second],data[:first])
    integration(data[:third],data[third:fourth],sorted(data[first:second]),data[:first])





