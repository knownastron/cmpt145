#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

#n is the number of rows in the triangle
n = 0

#gets the number of rows in the triangle from console input
while n < 1:
    n = int(input("Please enter the number of rows in the triangle "))
    if n < 1:
        print("There must be at least 1 row in the triangle. Try again")

def getTriangle():
    """
    Purpose: Asks users to input n lines of numbers and add them to a list that
             represents a Pascal triangle
    Pre-conditions: None
    Post-condition: None
    return: A list of lists that represents a Pascal triangle
    """
    triangle = []
    for i in range(n):
        #take in a string of numbers seperated by a space, split at each space
        #to create a list
        line = input("Please enter the numbers in line " + str(i+1) +
                     " separated by a space  ").split()
        #turn each string in the list into an integer
        line = [int(x) for x in line]
        #add the line of integers to the triangle
        triangle.append(line)
    return triangle

def checkTriangle(triangle):
    """
    Purpose: to check if the input triangle conforms to the rules of a Pascal
             triangle
    Pre-condition:
        :param triangle: a list of lists where each element is an integers
    Post-condition: None
    Return: True if the input triangle conforms to the rules of a Pascal triangle
            False if the outside numbers of the triangle is not 1 or the inside
            numbers do not equal the two numbers above it
    """
    #i represents the index of the line in the triangle
    for i in range(len(triangle)):
        lineLen = len(triangle[i])
        #loop through each element in the line
        for j in range(lineLen):
            #if j is the first or the last number in the row, it should equal 1
            if j == 0 or j == lineLen - 1:
                if triangle[i][j] != 1:
                    return False
            else:
                #else the number should equal the sum of the two numbers above
                if triangle[i][j] != triangle[i-1][j-1] + triangle[i-1][j]:
                    return False
    return True

triangle = getTriangle()

if checkTriangle(triangle):
    print('yes')
else:
    print('no')
