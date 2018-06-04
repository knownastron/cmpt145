# import sys

def readMaze(inFile):
	'''
	Purpose: read a file formatted as a rectangular grid of 0s and 1s 
	Pre-Condition: file contains rows of integers; input integers are in range 0..1
	Post-condition: none
	Return: a list containing n sublists of m integers each (nxm grid)
	'''
	mazeGrid = []
	lengthOK = True
	with open(inFile, "r") as ins:
		for line in ins:
			items = line.split()
			mazeGrid.append(items)
		ins.close()
	cols = len(mazeGrid[0])
	rows = len(mazeGrid)
	return(mazeGrid,rows,cols)

def printMaze(Maze):
	for r in range(len(Maze)):
		for c in range(len(Maze[0])):
			print(Maze[r][c]," ",end='')
		print('')

def SolveMaze(theMaze,startLoc,goalLoc):
	'''
	Purpose: Given a maze 'theMaze' with start tuple 'startLoc' and end tuple 'goalLoc' where each tuple is in form (row,col) 
	         determine if a path exists through the maze from startLoc to goalLoc. Print maze and return TRUE if a path exists; FALSE otherwise.
	Pre-Condition: maze is a list of lists containing only '0' and '1' to indicate available or blocked locations. 
	         startLoc and goalLoc are tuples in the form (row,col).
	Post-condition: none
	Return: true if a path exists, false otherwise
	'''
	srow = startLoc[0]
	scol = startLoc[1]
	grow = goalLoc[0]
	gcol = goalLoc[1]

	# base case current startloc is unavailabl
	# print(srow,scol,grow,gcol)
	if (srow < 0 or srow > len(theMaze)-1): return (False)    #outside horizontal boundaries
	if (scol < 0 or scol > len(theMaze[0])-1): return (False) #outside vertical boundaries
	if (theMaze[srow][scol] != '0'): return (False)         # start location is blocked
	# mark location as occupied
	theMaze[srow][scol] = 'X'
	if (srow == grow) and (scol == gcol): 
		printMaze(theMaze)
		return (True)                                       # maze has been solved
    # try the different directions
	if (SolveMaze(theMaze,(srow,scol+1),goalLoc)): return(True)   # try east
	if (SolveMaze(theMaze,(srow,scol-1),goalLoc)): return(True)   # try west
	if (SolveMaze(theMaze,(srow-1,scol),goalLoc)): return(True)   # try north
	if (SolveMaze(theMaze,(srow+1,scol),goalLoc)): return(True)   # try south
	# unmark the path
	theMaze[srow][scol] = '0'
	return (False)  # failed to find a path in any direction

def SolveMaze2(theMaze,startLoc,goalLoc):
	'''
	Purpose: Given a maze 'theMaze' with start tuple 'startLoc' and end tuple 'goalLoc' where each tuple is in form (row,col) 
	         determine if a path exists through the maze from startLoc to goalLoc. Print maze and return TRUE if a path exists; FALSE otherwise.
	Pre-Condition: maze is a list of lists containing only '0' and '1' to indicate available or blocked locations. 
	         startLoc and goalLoc are tuples in the form (row,col).
	Post-condition: none
	Return: true if a path exists, false otherwise
	'''
	
	srow = startLoc[0]
	scol = startLoc[1]
	grow = goalLoc[0]
	gcol = goalLoc[1]

	# base case current startloc is unavailabl
	# print(srow,scol,grow,gcol)
	if (srow < 0 or srow > len(theMaze)-1): return (False)    #outside horizontal boundaries
	if (scol < 0 or scol > len(theMaze[0])-1): return (False) #outside vertical boundaries
	if (theMaze[srow][scol] != '0'): return (False)         # start location is blocked

	# this solution duplicates the maze with a path location and solves the new maze. Much more resource intensive but does not mess with original maze
	# do not expect students to know about deep copying so will handle the copying right here as a loop
	theMazeCopy = []
	for i in range(len(theMaze)):
		innerCopy = []
		for j in range(len(theMaze[0])):
			# append new element into inner list
			innerCopy.append(theMaze[i][j])
		theMazeCopy.append(innerCopy)
	
	# mark location as occupied
	theMazeCopy[srow][scol] = 'X'

	#print("The copy:",srow,scol,"theMaze is theMazeCopy",theMaze is theMazeCopy)
#	printMaze(theMazeCopy)
	if (srow == grow) and (scol == gcol): 
		printMaze(theMazeCopy)
		return (True)                                       # maze has been solved
    # try the different directions
	
	if (SolveMaze2(theMazeCopy,(srow,scol+1),goalLoc)): return(True)   # try east
	if (SolveMaze2(theMazeCopy,(srow,scol-1),goalLoc)): return(True)   # try west
	if (SolveMaze2(theMazeCopy,(srow-1,scol),goalLoc)): return(True)   # try north
	if (SolveMaze2(theMazeCopy,(srow+1,scol),goalLoc)): return(True)   # try south
	
	return (False)  # failed to find a path in any direction

def putPathInMaze(theMaze,pathList):
	'''
	Purpose: Given a maze 'theMaze' and a path list 'pathList', put an 'X' into each location of the maze on the path list
	Pre-Condition: maze is a list of lists containing only '0' and '1' to indicate available or blocked locations. 
	         pathList is a list of tuples of form (row,col) representing locations on the path.
	Post-condition: theMaze is modified to contain Xs showing the path
	Return: nothing
	'''
	
	for n in range(len(pathList)):
		rowColTuple = pathList[n]
		row = rowColTuple[0]
		col = rowColTuple[1]
		theMaze[row][col] = 'X'

def onThePath(pathList,startLoc):
	for n in range(len(pathList)):
		if (pathList[n] == startLoc):
			return(True)
	return (False)

def SolveWithSeparatePath(theMaze,startLoc,goalLoc,pathList):
	'''
	Purpose: Given a maze 'theMaze' with start tuple 'startLoc' and end tuple 'goalLoc' where each tuple is in form (row,col) 
	         determine if a path exists through the maze from startLoc to goalLoc. Print maze and return TRUE if a path exists; FALSE otherwise.
	Pre-Condition: maze is a list of lists containing only '0' and '1' to indicate available or blocked locations. 
	         startLoc and goalLoc are tuples in the form (row,col), pathList is a list of tuples (row,col) representing location where we have
			 been.
	Post-condition: none
	Return: true if a path exists, false otherwise
	'''
	srow = startLoc[0]
	scol = startLoc[1]
	grow = goalLoc[0]
	gcol = goalLoc[1]

	# base case current startloc is unavailabl
	# print(srow,scol,grow,gcol)
	if (srow < 0 or srow > len(theMaze)-1): return (False)    #outside horizontal boundaries
	if (scol < 0 or scol > len(theMaze[0])-1): return (False) #outside vertical boundaries
	if (theMaze[srow][scol] != '0' or onThePath(pathList,startLoc)): return (False)         # start location is blocked or already on path

	# add location to path list
	pathList.append(startLoc)
	
	if (srow == grow) and (scol == gcol):
		putPathInMaze(theMaze,pathList)
		printMaze(theMaze)
		return (True)                                       # maze has been solved
    # try the different directions
	
	if (SolveWithSeparatePath(theMaze,(srow,scol+1),goalLoc,pathList)): return(True)   # try east
	if (SolveWithSeparatePath(theMaze,(srow,scol-1),goalLoc,pathList)): return(True)   # try west
	if (SolveWithSeparatePath(theMaze,(srow-1,scol),goalLoc,pathList)): return(True)   # try north
	if (SolveWithSeparatePath(theMaze,(srow+1,scol),goalLoc,pathList)): return(True)   # try south
	
	# remove startLoc from pathList
	pathList.remove(startLoc)
	return (False)  # failed to find a path in any direction


def SolveMaze3(theMaze,startLoc,goalLoc):
	'''
	Purpose: Given a maze 'theMaze' with start tuple 'startLoc' and end tuple 'goalLoc' where each tuple is in form (row,col) 
	         determine if a path exists through the maze from startLoc to goalLoc. Print maze and return TRUE if a path exists; FALSE otherwise.
	Pre-Condition: maze is a list of lists containing only '0' and '1' to indicate available or blocked locations. 
	         startLoc and goalLoc are tuples in the form (row,col).
	Post-condition: none
	Return: true if a path exists, false otherwise
	'''
	pathList = []
	return (SolveWithSeparatePath(theMaze,startLoc,goalLoc,pathList))


# ----------- MAIN ---------------
print("Opening the file....")
getMaze,rowcnt,colcnt = readMaze("G:\Cyril\COMP145_2018\Assignments\A7\maze3.txt") # maze 1: (0,3)(4,5), maze 2: (0,0)(8,9), maze 3: (3,0)(23,30)
#result = SolveMaze(getMaze,(3,0),(23,30))
#result = SolveMaze2(getMaze,(3,0),(23,30))
result = SolveMaze3(getMaze,(3,0),(23,30))
print(result)

