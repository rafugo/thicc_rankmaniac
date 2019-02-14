#! /bin/bash

# first, run it once
python pagerank_map.py < input.txt | sort | python pagerank_reduce.py |
python process_map.py | sort | python process_reduce.py > output.txt

i="0"

# run a while loop for 49 more iters
while [ $i -lt 49 ];
do
    echo $i
    # writes and reads to/from output.txt
    python pagerank_map.py < output.txt | sort | python pagerank_reduce.py |
python process_map.py | sort | python process_reduce.py > output_copy.txt

    # move the output back to output.txt
    mv output_copy.txt output.txt

    # exit once it writes the final ranks to the output file
    grep -q "FinalRank" output.txt
    if [ $? -eq 0 ]
    then
        echo "\nfinal ranks outputted"
        exit 1
    fi

    i=$[$i+1]
    
done
echo "max iterations reached"