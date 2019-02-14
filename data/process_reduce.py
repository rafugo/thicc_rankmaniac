#!/usr/bin/env python

import sys
from operator import itemgetter

#
# This program simply represents the identity function.
#


change = 0

rows = []
rowsNumbers = []


top500_new = []
top500_old = []
mintuple_new = []
mintuple_old = []

for line in sys.stdin:
    adjacency_row = []

    # split string input
    node_id, value = line.split("\t")


    # split into list
    value_list = value.split(',')
    # make list of values floats
    for i in range(len(value_list)):
        if i <= 1:
            adjacency_row.append(float(value_list[i]))
        else:
            adjacency_row.append(int(value_list[i]))
    
    

    # get ranks
    new = adjacency_row[0]
    old = adjacency_row[1]

    # make row for sorting/finding top 20
    rowI = [node_id, new, old]

    if len(top500_new) != 500:
        top500_new.append(rowI)
        top500_old.append(rowI)

        if mintuple_new == []:
            mintuple_new = rowI
            mintuple_old = rowI

        else:
            if mintuple_new[1] > rowI[1]:
                mintuple_new = rowI
            if mintuple_old[2] > rowI[2]:
                mintuple_old = rowI

    else:
        if mintuple_new[1] < rowI[1]:
            top500_new.remove(mintuple_new)
            top500_new.append(rowI)
            mintuple_new = rowI

            # get new min
            for j in top500_new:
                if j[1] < mintuple_new[1]:
                    mintuple_new = j
        # do the same for the last top 20
        if mintuple_old[2] < rowI[2]:
            top500_old.remove(mintuple_old)
            top500_old.append(rowI)
            mintuple_old = rowI

            # get new min
            for j in top500_old:
                if j[1] < mintuple_old[1]:
                    mintuple_old = j


    neighbors = ''
    for i in range(len(adjacency_row)):
        if i > 1:
            neighbors += ',' + str(adjacency_row[i])

    # keep track in case we need to keep going
    final_row = 'NodeId:' + node_id + '\t' + \
                            str(new) + ',' + str(old) + neighbors
                            

    # for printing
    rows.append(final_row)
    rowsNumbers.append(rowI)

    # accumulate the change
    change += abs(new - old)

top500_new = sorted(top500_new, key=itemgetter(1))[::-1]
top500_old = sorted(top500_old, key=itemgetter(1))[::-1]

# once we read in all the output, determine if we stop
if top500_old == top500_new:

    for i in range(len(top500_new)):
        sys.stdout.write("FinalRank:" + str(top500_new[i][1]) + '\t' + \
                            str(top500_new[i][0]) + '\n')

else:
    # output so we can restart
    for line in rows:
        sys.stdout.write(line + '\n')
