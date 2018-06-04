import node as node


# create the chain of nodes
# chain-->[ 3 | *-]-->[ 2 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]

chain = node.create(4, next=None)
chain = node.create(5, chain)
chain = node.create(1, chain)
chain = node.create(2, chain)
chain = node.create(3, chain)



# Exercises:
# Remove the 3 from the sequence

chain = node.get_next(chain)

# Add 6 to the front

chain = node.create(6, chain)

# add 7 to the end
anode = node.create(7)

bnode = chain
while node.get_next(bnode) != None:
    bnode = node.get_next(bnode)

node.set_next(bnode, anode)



# Extra exercises:
# Exercise 1
# Display all numbers in the chain
# Turn this code into a function!
# chain-->[ 3 | *-]-->[ 2 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]



# Exercise 2
# Count the even numbers
# chain-->[ 3 | *-]-->[ 2 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]
# anode --------------------------^



# Exercise 3
# Check if the data values 2, 9 are in the chain
# Turn this code into a function!
# chain-->[ 3 | *-]-->[ 2 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]

# Exercise 4
# Put a new node with data value 8 between 2 and 1
# Turn this code into a function!
# Before:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]
# After:   chain-->[ 3 | *-]-->[ 2 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]


# Exercise 5
# Put a new node with data value 10 before the 3rd node in the chain
# Turn this code into a function!
# Before:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]
# After:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 10 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]

# Exercise 6
# Remove the 4 from the sequence (assuming no reference to the end of the chain)
# Before:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | *-]-->[ 4 | / ]
# After:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 10 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | / ]



# Exercise 7
# Change the list so that 8 follows 2, and the node with data value 1 is no longer in the chain
# Turn this code into a function that deletes a node at a given index
# Turn this code into a function that deletes a node with a give data value
# Before:  chain-->[ 3 | *-]-->[ 2 | *-]-->[ 10 | *-]-->[ 8 | *-]-->[ 1 | *-]-->[ 5 | / ]
# After:   chain-->[ 3 | *-]-->[ 2 | *-]-->[ 10 | *-]-->[ 8 | *-]-->[ 5 | / ]


