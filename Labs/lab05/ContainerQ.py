# CMPT 145: ADTs
# Simple adapter for Queues

import Queue as Queue

def create():
    return Queue.create()
def add(container,value):
    Queue.enqueue(container,value)
def remove(container):
    return Queue.dequeue(container)
def is_empty(container):
    return Queue.is_empty(container)
def size(container):
    return Queue.size(container)

