#!/bin/bash -e
#SBATCH -t 1:30 -N 1 -n 2 --mem=2000M
echo "#define SIZE_N 23000"
echo "#define BLOCK_SIZE 100"
echo "#define R_MULTIPLIER 130"

export OMP_NUM_THREADS=`nproc --all`
echo "CORES=2"
mpirun -np 2 ./assignment
