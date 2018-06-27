#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

# CMPT 145: ADTs
# Simple adapter for Stacks

import Stack as Stack

def create():
    return Stack.create()
def add(container,value):
    Stack.push(container,value)
def remove(container):
    return Stack.pop(container)
def is_empty(container):
    return Stack.is_empty(container)
def size(container):
    return Stack.size(container)
