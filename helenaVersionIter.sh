#!/bin/bash

# This script runs a Map, Reduce, Map, Reduce sequence a maximum of max_iter
# times or until FinalRank is output. The initial data must be in input.txt

# HOW TO USE:
# Run this script with these files in the same directory as this script:
# pagerank_map.py, pagerank_reduce.py, process_map.py, process_reduce.py, input.txt

input_file='input.txt'
max_iter=50
i=1
python pagerank_map.py < $input_file | sort -k1,1 | python pagerank_reduce.py | python process_map.py | sort -k1,1 | python process_reduce.py > temp.txt
echo 'Iteration '$i' done'
[ -e output.txt ] && rm output.txt
cp temp.txt output.txt
while [ $i -le $max_iter ]
do

if [ $i -ge $max_iter ]
then
	echo 'Failed to find final ranks after '$max_iter' iterations'
	break
fi

if grep -q FinalRank output.txt
then
	rm temp.txt
	echo 'Final ranks written to output.txt'
	break
fi

()i++))
python pagerank_map.py < temp.txt | sort -k1,1 | python pagerank_reduce.py | python process_map.py | sort -k1,1 | python process_reduce.py > output.txt
echo 'Iteration '$i' done'

rm temp.txt
cp output.txt temp.txt
done