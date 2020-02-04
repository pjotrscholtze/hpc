#!/bin/bash -e
#SBATCH -t 0:10 -N 1 -n 1 --mem=2000M

export OMP_NUM_THREADS=`nproc --all`

echo "#define SIZE_N 23000"
echo "#define BLOCK_SIZE 100"
echo "#define R_MULTIPLIER 130"

mpirun -np 1 ./assignment
