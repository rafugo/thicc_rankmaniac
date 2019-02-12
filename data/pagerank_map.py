#!/usr/bin/env python

import sys

alpha = .85

for line in sys.stdin:
    # Split the line on the tab and grab id and the list that follows.
    l = line.strip().split("\t")
    node_id = l[0][7:]
    adjacency_row = l[1].split(",")
    
    # If there are neighbors, grab them, and the node's rank. 
    if len(adjacency_row) > 2:
        neighbors = adjacency_row[2:]
        rank = float(adjacency_row[0])
        contribution = alpha * rank / float(len(neighbors))
        for node in neighbors:
            sys.stdout.write("%s\t%f" % (node, contribution) + "\n")
    sys.stdout.write("%s\t%s" % (node_id, adjacency_row) + "\n")

