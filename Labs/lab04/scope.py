# CMPT 145: Scope Laboratory



def find_duplicates(alist):
    """
    Purpose:
        Return a list of duplicate values found in alist.
    Pre:
        :param alist: a list of values
    Post:
        None
    Return:
        A list of duplicates from alist
    """
    uniques = []
    for item in alist:
        if item in uniques:
            print(duplicates)
            duplicates.append(item)
        else:
            uniques.append(item)
    return duplicates

# a global variable
duplicates = []
