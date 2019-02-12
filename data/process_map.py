#!/usr/bin/env python

import sys
import ast

#
# This program simply represents the identity function.
#
s = 0
t = 0
for line in sys.stdin:
    t += 1
    # split string input
    node_id, value = line.split("\t")

    firstIter = False

    # change value into a variable from a string
    value = ast.literal_eval(value)

    s += float(value[0])

sys.stdout.write(str(s) + '\n')
sys.stdout.write(str(t) + '\n')

