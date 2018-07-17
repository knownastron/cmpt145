#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

def fib(n):
    """
    Purpose:
    Pre-condition:
    Post-condition:
    return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def moos(n):
    """
    Purpose:
    Pre-condition:
    Post-condition:
    return:
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moos(n-1) + moos(n-2) + moos(n-3)


def substr(old, new, string):
    """
    Purpose:
    Pre-condition:
    Post-condition:
    return:
    """

    new_string = "";
    if string == "":
        return new_string
    elif string[0] == old:
        new_string += new
    else:
        new_string += string[0]
    return new_string + substr(old, new, string[1:])


for i in range(11):
    print(moos(i))
