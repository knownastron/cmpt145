# CMPT 145: Linear ADTs
# A simple demonstration of the Queue ADT
#

import Queue as Queue

# create the queue
data = Queue.create()


# add some data to the queue
for v in range(1,6):
    Queue.enqueue(data, v)

val = Queue.peek(data)
print("Peeked and found:", val)

# remove all the data one value at a time
while not Queue.is_empty(data):
    d = Queue.dequeue(data)
    print(d)


