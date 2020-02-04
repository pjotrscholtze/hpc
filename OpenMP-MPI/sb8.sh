#!/bin/bash -e
#SBATCH -t 1:30 -N 1 -n 8 --mem=2000M
echo "#define SIZE_N 23000"
echo "#define BLOCK_SIZE 100"
echo "#define R_MULTIPLIER 130"

export OMP_NUM_THREADS=`nproc --all`
echo "CORES=8"
mpirun -np 8 ./assignment
