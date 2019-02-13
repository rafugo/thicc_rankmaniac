#!/usr/bin/env python

import sys

counter = 0
top20 = []
for line in sys.stdin:
    counter += 1

    node_id, value = line.split("\t")

    idNum = node_id[7:]

    if counter <= 20:
        top20.append((idNum, 1.0))


for i in range(len(top20)):
    sys.stdout.write('FinalRank:' + str(top20[i][1]) + '\t' + str(top20[i][0]) + '\n')
    