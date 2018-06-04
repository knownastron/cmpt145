# File: magic.py
# Author: CMPT 145
# Version: 1.0


#############################
# 3x3 Magic Square Detection 
# Design Document
#
# 1. Application's Purpose:
#   To determine if a given arrangement of 9 numbers 
#   is a magic square or not.  
#   **Note: this program does not try to create a magic square!
#
# 2. Magic Square Definition: 
#   - 3x3 grid  
#   - contains integers 1 through 9 
#   - every integer in 1-9 must appear exactly once
#   - all rows, columns, and diagonals of the grid add up to 15
#
#   E.g.  Magic   not Magic
#         8 1 6     1 9 6
#         3 5 7     5 3 7
#         4 9 2     4 8 2
# 
# 
# 3. High level behaviour (main)
#   Ask for the sequence of numbers ("square")
#   Check whether it is magic!
#   Program should display "Yes" if it's magic, "no" otherwise
#############################




############################
def get_square():
	'''
	Get a square of 9 integers from the console.
	#   Inputs: none
	#   Uses console input to obtain 9 numbers from the console
	#   Return: Returns a 3x3 list of lists with the numbers in it
	'''
	input_values = input('Please enter 9 integers from 1 to 9 inclusive: ')
	values = input_values.rstrip().split()	
	square = [ [int(values[3*i+j]) for j in range(3)] for i in range(3)]
	return square
	




#############################
def check_range(square):
  '''Check that the square contains all the numbers 1 ... 9
#   Inputs: given a 3x3 list of integers
#   Return: True if the square contains all the integers 1 .. 9
#           False otherwise
  '''
  # seen is a list of booleans, to record values observed in the square
  seen = 9*[False]
 
  # check for repeated numbers 
  for i in range(3):
    for j in range(3):
      val = square[i][j]
      # has val been seen before?
      if val > 0 and val < 10 and not seen[val-1]:
        # no, so we mark it seen now
        seen[val-1] = True
      else:
        # yes, so it must be a repeated number
        return False

  # check that all the numbers were seen.
  for i in range(9):
    if not seen[i]:
      return False

  # no repeats, and all numbers seen
  return True


#############################
def check_rows(square):
    '''Check that the rows of the square sum to 15.
#   Inputs: given a 3x3 list of integers
#   Return: True if all the rows sum to 15
#           False otherwise
    '''
    for row in square:
      if sum(row) != 15:
        return False
    return True


#############################
def check_columns(square):
  '''Check that the columns all sum to 15.
#   Inputs: given a 3x3 list of integers
#   Return: True if all the columns sum to 15
#           False otherwise
  '''
#  1. check the sum of the values from first column
#  2. check the sum of the values from second column
#  3. check the sum of the values from third column
#  4. if any one of the checks resulted in an incorrect sum, return False
#     otherwise, return True
  for j in range(3):
    if sum([square[i][j] for i in range(3)]) != 15:
      return False
  return True


#############################
def check_diagonals(square):
  '''Check that the diagonals sum to 15.
#   Inputs: given a 3x3 list of integers
#   Return: True if all the diagonals sum to 15
#           False otherwise
        '''
#  1. check the sum of the values from upward diagonal
#  2. check the sum of the values from downward diagonal
#  3. if any one of the checks resulted in an incorrect sum, return False
#     otherwise, return True
  upwards   = sum([square[i][i]   for i in range(3)])
  downwards = sum([square[i][2-i] for i in range(3)])
  return upwards == 15 and downwards == 15


#############################
def check_square(square):
  '''Check the square for all its 'magic' properties.
#   Inputs: given a 3x3 list of integers
#   Return: True if the square has all the properties of a magic
#           square; False otherwise
  '''
  return check_range(square) and \
         check_rows(square) and \
         check_columns(square) and \
         check_diagonals(square)


############################
# main script

square = get_square()
if check_square(square):
  print('Yes!')
else:
  print('No!!')


