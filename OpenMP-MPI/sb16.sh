#!/bin/bash -e
#SBATCH -t 0:10 -N 1 -n 16 --mem=2000M

echo "#define SIZE_N 23000"
echo "#define BLOCK_SIZE 100"
echo "#define R_MULTIPLIER 130"

export OMP_NUM_THREADS=`nproc --all`
echo "OMP_NUM_THREADS="$OMP_NUM_THREADS
mpirun -np 16 ./assignment
