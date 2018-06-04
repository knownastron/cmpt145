# CMPT 145: Assignment 3
# A command line app to count characeters in a text file

import a3q3 as Counter
import sys as sys

counter = Counter.create()

# open the file and count the contents
infile = open(sys.argv[1])
for line in infile:
    line = line.rstrip()
    for letter in line:
        Counter.see(counter, letter)

# now report
print('There were:', Counter.total(counter), 'letters in total')
print('There were:', Counter.size(counter), 'unique letters:')

for val in Counter.unique(counter):
    print(val, ':', Counter.seen(counter, val))

# all done
