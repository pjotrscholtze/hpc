#!/bin/python3

BLOCK_SIZE = 64
R_SIZES = [10, 1000, 100000, 10000000]
N_SIZES = [1000, 2000, 10000, 20000]


# <block_size> <r_size> <n_size>
def make_sb_sh(block_size, r_multiplier, size_n, cores):
    contents =  """#!/bin/bash -e
#SBATCH -t 1:30 -N 1 -n $4 --mem=2000M

echo "#define SIZE_N $3"
echo "#define BLOCK_SIZE $1"
echo "#define R_MULTIPLIER $2"
export OMP_NUM_THREADS=`nproc --all`
echo "CORES=$4"
mpirun -np 1 ./assignment_$1_$2_$3
""".replace("$1", block_size)
    contents = contents.replace("$2", r_multiplier)
    contents = contents.replace("$3", size_n)
    contents = contents.replace("$4", cores)
    filename = "sb$4_$1_$2_$3.sh".replace("$1", block_size) 
    filename = filename.replace("$2", r_multiplier)
    filename = filename.replace("$3", size_n)
    filename = filename.replace("$4", cores)
    with open(filename, "w") as f:
        f.writelines([contents])




def make_sba_part(block_size, r_multiplier, size_n):
    t = """
python3 ./set_block_size.py $1 $2 $3
rm assignment
make assignment
mv assignment assignment_$1_$2_$3

#sbatch ./sb1_$1_$2_$3.sh
sbatch ./sb2_$1_$2_$3.sh
sbatch ./sb4_$1_$2_$3.sh
sbatch ./sb8_$1_$2_$3.sh
sbatch ./sb16_$1_$2_$3.sh
""".replace("$1", block_size)
    t = t.replace("$2", r_multiplier)
    t = t.replace("$3", size_n)
    return t



job_count = len(N_SIZES) * len(R_SIZES)

sba_content = ""
i = 0
for r in R_SIZES:
    for n in N_SIZES:
        sba_content += "echo '#############'"
        sba_content += "echo '#############'"
        sba_content += "echo '###       ###'"
        sba_content += "echo '### %.2f ###'" % ((i / job_count) * 100)
        sba_content += "echo '###       ###'"
        sba_content += "echo '#############'"
        sba_content += "echo '#############'"
        sba_content += make_sba_part(str(BLOCK_SIZE), str(r), str(n))

        for core in [2, 4, 8, 16]:
            make_sb_sh(str(BLOCK_SIZE), str(r), str(n), str(core))
        i += 1



with open("sba_multi.sh", "w") as f:
    f.writelines([sba_content])
