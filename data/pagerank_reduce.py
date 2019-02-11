#!/usr/bin/env python

import sys
import re

alpha = 0.85

for line in sys.stdin:
    # split string input into node id and neighbors & contributions from other nodes
    node_id, values = line.split("\t")
    
    # make values a list where neighbors is a nested 
    neighbors = []
    neighbors_values = re.findall("\[([^[\]]*)\]", values)
    neighbors_split = neighbor_values[0].split(',') # returns in the form ['a', 'b', 'c']
    for neigh in neighbors_split:
        neighbors.append(int(neigh))
    contribution_values = values.replace(neighbor_values[0], '') # makes neighbor list ' []'
    contributions_split = values.split(',') # split string into list
    contributions = []
    for contrib in contributions_split: # weed out ' []' and make rest ints
        if contrib != ' []':
            contributions.append(float(contrib))
    
    # initialize the new rank variable
    new_rank = 0
    
    # iterate through list, summing up contributions
    for n in contributions:
        new_rank += n
    
    # evaluate new rank using alpha NOT FINAL DOES NOT USE N
    new_rank = alpha * new_rank
    
    # update current and old rank in neighbors list
    new_oldrank = neighbors[0]
    neighbors[0] = new_rank
    neighbors[1] = new_oldrank
    
    # make output string to write out
    new_line = node_id + "\t" + str(neighbors)
    sys.stdout.write(line)

