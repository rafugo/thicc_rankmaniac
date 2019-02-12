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

    # if we just saw a new node, we gotta print what we have
    elif previousNode != node_id:
        # once done processing, multiply by alpha
        columnSum = alpha * columnSum

        # set as new rank (temporarily)
        adjacency_row[0] = columnSum

        # create the output string
        output = 'NodeId:' + previousNode + '\t' + str(adjacency_row) + '\n'

        # emit the row
        sys.stdout.write(output)

        # clear the values
        adjacency_row = []
        columnSum = 0
        previousNode = node_id



    firstIter = False

    # change value into a variable from a string
    value = ast.literal_eval(value)

    # check if it's the row of the adjacency list
    # or a value to sum
    if isinstance(value, list):
        adjacency_row = list(value)

    else:
        columnSum += float(value)

# once done processing, multiply by alpha
columnSum = alpha * columnSum

# set as new rank (temporarily)
adjacency_row[0] = columnSum

# create the output string
output = 'NodeId:' + node_id + '\t' + str(adjacency_row) + '\n'

# emit the row
sys.stdout.write(output)

