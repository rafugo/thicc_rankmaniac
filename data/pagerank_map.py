#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
	# Split the line on the tab and grab id and the list that follows.
	l = line.split("\t")
	node_id = l[0][7:]
	lst = l[1].split(",")
	# If there are neighbors, grab them, and the node's rank. 
	if len(lst) > 2:
		neighbors = lst[2:]
		rank = lst[0]
		for node in neighbors:
			sys.stdout.write("(%s, %d)" % node, rank / len(neighbors))
    sys.stdout.write("(%s, [%s])" % node_id, lst)

