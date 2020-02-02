#!/bin/bash -e
#SBATCH -t 0:10 -N 1 -n 8 --mem=2000M

export OMP_NUM_THREADS=`nproc --all`
mpirun -np 8 ./assignment
