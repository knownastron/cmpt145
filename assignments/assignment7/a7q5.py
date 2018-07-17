#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

def fib(n):
    """
    Purpose:
        get the nth number of the fibonacci sequence
    Pre-condition:
        :param n: a positive integer
    return:
        an integer representing the nth number of teh fibonacci sequence
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
        get the nth number of the Moosonacci sequence
    Pre-condition:
        :param n: a positive integer
    return:
        an integer representing the nth number of teh Moosonacci sequence
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
        replace all instances of the old letter with the new letter in the
        input string
    Pre-condition:
        :param old: a string character of desired target character in string
        :param new: a string character of desired replacement character in string
        :param string: a string
    return:
        a new string with all instances of old replaced with new
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
