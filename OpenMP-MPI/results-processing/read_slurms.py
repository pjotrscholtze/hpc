#!/bin/python3
from glob import glob
from typing import List
class Result:
    def __init__(self, size_n: int, block_size: int, r_multiplier: int, 
        cores: int, error: bool, time: str):
        self.size_n = size_n
        self.block_size = block_size
        self.r_multiplier = r_multiplier
        self.cores = cores
        self.error = error
        self.time = time

def _parse_slurm(path: str) -> Result:
    content = ""
    size_n = 0
    block_size = 0
    r_multiplier = 0
    cores = 0
    error = True
    time = ""
    res = None
    with open(path, "r") as f:
        for line in f.readlines():
            if "#define " in line or "CORES=" in line:
                if line.startswith("#define SIZE_N"):
                    size_n = int(line[len("#define SIZE_N"):].strip())

                if line.startswith("#define BLOCK_SIZE"):
                    block_size = int(line[len("#define BLOCK_SIZE"):].strip())

                if line.startswith("#define R_MULTIPLIER"):
                    r_multiplier = int(line[len("#define R_MULTIPLIER"):].strip())

                if line.startswith("CORES="):
                    cores = int(line[len("CORES="):].strip())
            if "seconds" in line:
                # time = line[len("Master has finished. This took"):].strip()
                # time = time.split(" ")[0]
                raw = line.split(" ")
                time = raw[len(raw) - 2]
                error = False
        res = Result(size_n, block_size, r_multiplier, cores, error, time)
        if res.cores==2:
            print(res.__dict__)
    return res


def get_results() -> List[Result]:
    results = []
    for path in glob("/home/pjotr/slurms/*"):
        results += [_parse_slurm(path)]
    return results


get_results()