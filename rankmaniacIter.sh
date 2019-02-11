#! /bin/bash


python pagerank_map.py < input.txt | sort | python pagerank_reduce.py |

for i in `seq 1 10`;
do
    python pagerank_map.py | sort | python pagerank_reduce.py |
    python process_map.py | sort | python process_reduce.py
done

python process_map.py | sort | python process_reduce.py > output.txt
