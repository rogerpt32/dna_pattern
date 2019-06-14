#!/bin/bash

cd ../src/
make clean
make

# for i in `seq 1 32`;
# do
#     echo -ne "$i/32"\\r
#     ./generator $i ../data/input.txt
#     ./bruteforce ../data/full_genome.txt "$(< ../data/input.txt)" > ../results/bruteforce_$i.txt
#     ./horspool ../data/full_genome.txt "$(< ../data/input.txt)" > ../results/horspool_$i.txt
#     ./BNDM ../data/full_genome.txt "$(< ../data/input.txt)" > ../results/BNDM_$i.txt
#     ./BOM ../data/full_genome.txt "$(< ../data/input.txt)" > ../results/BOM_$i.txt
# done

for i in `seq 1 32`;
do
    echo -ne "$i/32"\\r
    ./generator $i ../data/input.txt
    ./bruteforce ../data/test.txt "$(< ../data/input.txt)" > ../results/bruteforce_$i.txt
    ./horspool ../data/test.txt "$(< ../data/input.txt)" > ../results/horspool_$i.txt
    ./BNDM ../data/test.txt "$(< ../data/input.txt)" > ../results/BNDM_$i.txt
    ./BOM ../data/test.txt "$(< ../data/input.txt)" > ../results/BOM_$i.txt
done

rm ../data/input.txt
cd ../scripts/
python3 create_csv.py
# rm ../results/*.txt

