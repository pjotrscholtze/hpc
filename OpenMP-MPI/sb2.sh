#!/bin/bash -e
#SBATCH -t 0:10 -N 1 -n 2 --mem=2000M

export OMP_NUM_THREADS=`nproc --all`
mpirun -np 2 ./assignment
