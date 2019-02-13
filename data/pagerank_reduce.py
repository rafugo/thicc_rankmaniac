#!/usr/bin/env python

import sys
import ast

alpha = 0.85
adjacency_row = []
columnSum = 0

previousNode = ''
firstIter = True

for line in sys.stdin:
    # split string input
    node_id, value = line.split("\t")

    # first iteration, set the node id
    if firstIter:
        previousNode = node_id
        firstIter = False


    # if we just saw a new node, we gotta print what we have
    if previousNode != node_id:
        # once done processing, multiply by alpha and add 1 - alpha
        columnSum = columnSum + (1 - alpha)

        # set as new rank (temporarily)
        adjacency_row[0] = str(columnSum)

        output = previousNode + '\t'

        # create the output string
        for i in range(columnSum):
            output += columnSum[i] + ','

        output = output[:-1] + '\n'

        # emit the row
        sys.stdout.write(output)

        # clear the values
        adjacency_row = []
        columnSum = 0
        previousNode = node_id

    # check if it's an adjacency row
    if value[0] == '|':
        # get it as a list
        adjacency_row = value[1:].split()

    else:
        columnSum += float(value)

# once done processing, multiply by alpha and add 1 - alpha
columnSum = columnSum + (1 - alpha)

# set as new rank (temporarily)
adjacency_row[0] = str(columnSum)

output = previousNode + '\t'

# create the output string
for i in range(columnSum):
    output += columnSum[i] + ','

output = output[:-1] + '\n'

# emit the row
sys.stdout.write(output)

