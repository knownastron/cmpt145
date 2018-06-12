#Name: Jason Tran
#NSID: jat687
#Student Number: 11101081
#Course: CMPT 145-01
#Lab: L03

# Assignment 4 Question 1

import sys
import TStack as Stack
import TQueue as Queue



cases = []

file_name = sys.argv[1]
file = open(file_name, "r")
line = file.readline().rstrip().split()

while line:
    cases.append(line)
    line = file.readline().rstrip().split()

#create dictionary to track each month:
months = {}

for index, line in enumerate(cases):
    non_urgent = Queue.create()
    urgent = Stack.create()

    for case in line:
        if case[:3] == 'URG':
            Stack.push(urgent, case)
        else:
            Queue.enqueue(non_urgent, case)

    months['Month ' + str(index +1)] = [urgent, non_urgent]

print(months['Month 1'])

#prints the cases per month
for group in months:
    cases_for_month = ''
    print(months[group][1])
    for i in range(len(months[group][1])):
        cases_for_month += str(Stack.pop(months[group][0]))
    # for k in range(len(months[group][1])):
    #     cases_for_month += Queue.dequeue(months[group])
    print(cases_for_month)
