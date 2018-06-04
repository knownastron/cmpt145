

def fibonacci(n):
    """
    Purpose:
        The Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, ...
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Fibonacci number, starting with fib(0) = 0
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def moosonacci(n):
    """
    Purpose:
        Calculate the nth Moosonacci number
        The Moosonacci numbers are: 0, 1, 2, 3, 6, 11, 20, 37, ...
    Preconditions:
        :param n: a non-negative integer
    Return:
        :return: the nth Moosonacci number, starting with moos(0) = 0
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moosonacci(n-1) + moosonacci(n-2) + moosonacci(n-3)


def substr(t, r, s):
    """
    Purpose:
        Return a string that has the same characters in s, except that
        every occurrence of character t is replaced by character r.
    Preconditions
        :param t: the target character to replace
        :param r: the replacement character
        :param s: a string
    Return
        :return: a new string with t replaced by r in s
    """
    if len(s)==0:
        return ''
    elif s[0] == t:
        return r + substr(t, r, s[1:])
    else:
        return s[0] + substr(t, r, s[1:])
