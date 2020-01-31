#!/bin/bash -e
#SBATCH -t 2:30 -N 1 -n 4 --mem=100M
export OMP_NUM_THREADS=`nproc --all`

module load pre2019
module load python/3.5.0
python ./testcores.py
# echo ">> [START] Running on 4 cores"
# mpirun -np 4 ./assignment
# echo ">> [STOP] Running on 4 cores"

# echo ">> [START] Running on 3 cores"
# mpirun -np 3 ./assignment
# echo ">> [STOP] Running on 3 cores"

# echo ">> [START] Running on 2 cores"
# mpirun -np 2 ./assignment
# echo ">> [STOP] Running on 2 cores"

# echo ">> [START] Running on 1 cores"
# mpirun -np 1 ./assignment
# echo ">> [STOP] Running on 1 cores"

