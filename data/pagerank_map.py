#!/usr/bin/env python

import sys

alpha = .85

for line in sys.stdin:
    # Split the line on the tab and grab id and the list that follows.
    l = line.strip().split("\t")
    node_id = l[0][7:]
    adjacency_row = l[1].split(",")
    adjacency_row[0] = float(adjacency_row[0])
    # Calculate the node's current rank
    rank = adjacency_row[0]
    # Update the old rank
    adjacency_row[1] = adjacency_row[0]

    # recreate the adjacency row, but with a | at the start so we know it's
    # an adjacency row
    adj_row_str = '|'
    for i in range(len(adjacency_row)):
        adj_row_str += str(adjacency_row[i]) + ','
    # take out last comma
    adj_row_str = adj_row_str[:-1]
    
    # If there are neighbors, grab them, and the node's rank. 
    if len(adjacency_row) > 2:
        neighbors = adjacency_row[2:]
        contribution = alpha * rank / float(len(neighbors))
    else:
        neighbors = []
        contribution = alpha
        sys.stdout.write("%s\t%f" % (node_id, contribution) + "\n")

    for node in neighbors:
        sys.stdout.write("%s\t%f" % (node, contribution) + "\n")

    # output the special adj row string
    sys.stdout.write("%s\t%s" % (node_id, adj_row_str) + "\n")

