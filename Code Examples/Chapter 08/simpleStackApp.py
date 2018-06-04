# CMPT 145: Linear ADTs
# A simple demonstration of the Stack ADT
#

import Stack as Stack

# create the stack
data = Stack.create()


# add some data to the stack
for v in range(1,6):
    Stack.push(data, v)

val = Stack.peek(data)
print("Peeked and found:", val)

# remove all the data one value at a time
while not Stack.is_empty(data):
    d = Stack.pop(data)
    print(d)

