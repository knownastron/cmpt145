#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03


n = 4 #number of rows and columns

def getSquare():
    """
    Purpose: get user input for n lines of the latin square
    Pre-conditions: n must be an integer greater than 1
    Post-condition: None
    Return: a list of n lists, each sublist includes n elements of integers
    """
    #create a list that will hold the n number of lines
    square = []

    #get user input of n numbers per line
    for i in range(n):
        #take in a string of numbers seperated by a space, split at each space
        #to create a list
        line = input("Please input " + str(n) +
                     " numbers separated by a space for line " + str(i+1) +
                     " of the Latin square: ").split()
        #turn each element in the line into an integer
        line = [int(x) for x in line]
        #append the list of n integers into the list square
        square.append(line)

    return square

def checkHorizontal(latin):
    """
    Purpose: Check that each row includes all the numbers required for a latin
             square
    Pre-condition:
        :param latin: a list of n lists each with n elements of integers
    Post-condition: None
    Return: True if each horizontal line in the input latin includes all n
            numbers required for a latin square
            False if each horizontal line in the input latin does not include
            all n numbers required for a latin square
    """
    #loop over each row in the latin square
    for i in range(len(latin)):
        #create a list of numbers 1 to n that should appear in each line
        numbers = [x + 1 for x in range(n)]
        #loop through each column in row i
        for k in range(len(latin[i])):
            #check if the current number is in the list numbers
            if latin[i][k] in numbers:
                #remove current number if it appears in list numbers
                numbers.remove(latin[i][k])
            else:
                #return False if current number does not appear in list numbers
                return False

    #return True if every element is checked without fail
    return True

def checkVertical(latin):
    """
    Purpose: Check that each column includes all the numbers required for a
             latin square
    Pre-condition:
        :param latin: a list of n lists each with n elements of integers
    Post-condition: None
    Return: True if each vertical line in the input latin includes all n
            numbers required for a latin square
            False if each vertical line in the input latin does not include
            all n numbers required for a latin square
    """
    #loop over each column in the latin square
    for i in range(len(latin[0])):
        #create a list of numbers 1 to n that should appear in each line
        numbers = [x + 1 for x in range(n)]
        #loop through each row in the column i
        for k in range(len(latin)):
            #check if the current number is in the list numbers
            if latin[k][i] in numbers:
                #remove current number if it appears in list numbers
                numbers.remove(latin[k][i])
            else:
                #return False if current number does not appear in list numbers
                return False
    #return True if every element is checked without fail
    return True



latin = getSquare()

if checkVertical(latin) and checkHorizontal(latin):
    print("yes")
else:
    print("no")
