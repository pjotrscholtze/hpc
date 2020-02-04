#!/bin/sh
python3 ./set_block_size.py $1 $2
rm assignment
make assignment

sbatch ./sb1.sh
sbatch ./sb2.sh
sbatch ./sb4.sh
sbatch ./sb8.sh
sbatch ./sb16.sh

