#!/usr/bin/env python

import sys

alpha = 0.85

inputDict = {}

for line in sys.stdin:
    # split the line
    node_id, value = line.strip().split('\t')

    # add to dictionary
    # if empty
    if inputDict.get(node_id) == None:
        inputDict[node_id] = [value]

    # if not empty
    else:
        inputDict[node_id].append(value)

# sys.stderr.write(str(inputDict) + '\n')

# go through the dictionary, find the column sums and the adjacency row
for key in inputDict:
    adj_str = ''
    columnSum = 0

    for value in inputDict[key]:
        # check if adjacency row
        if value[0] == '|':
            adj_str = value[1:]

        # otherwise, add it
        else:
            columnSum += float(value)

    # update the new rank
    adjacency_row = adj_str.split(',')
    adjacency_row[0] = alpha * columnSum + (1 - alpha)

    # create the output string
    output = key + '\t'
    for entry in adjacency_row:
        output += str(entry) + ','
    output = output[:-1] + '\n'

    sys.stdout.write(output)
    






