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
        adjacency_row[0] = columnSum

        # create the output string
        output = previousNode + '\t' + str(adjacency_row) + '\n'

        # emit the row
        sys.stdout.write(output)

        # clear the values
        adjacency_row = []
        columnSum = 0
        previousNode = node_id


    # change value into a variable from a string
    value = ast.literal_eval(value)

    # check if it's the row of the adjacency list
    # or a value to sum
    if isinstance(value, list):
        adjacency_row = value

    else:
        columnSum += value

# once done processing, add the 1 - alpha
columnSum = columnSum + (1 - alpha)

# set as new rank (temporarily)
adjacency_row[0] = columnSum

# create the output string
output = node_id + '\t' + str(adjacency_row) + '\n'

# emit the row
sys.stdout.write(output)

