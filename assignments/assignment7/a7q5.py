#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def substr(old, new, string):
    """

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
    print(fib(i))
