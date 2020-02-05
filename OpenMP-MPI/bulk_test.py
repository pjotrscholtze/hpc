#!/bin/python3
from typing import List
import time
import subprocess

SUBMISSION_DELAY = 0.5

n_sizes = [1000, 2000, 5000, 10000, 20000]
r_sizes = [1, 2, 5, 10, 100]

def get_divisors(number: int) -> List[int]:
    limit = int(number / 2)
    test = 1
    results = []
    while test < limit:
        if number % test == 0:
            results += [test]
        test += 1
    results += [number]

    return results

totals = 0

# block_sizes = get_divisors(min(n_sizes))
block_sizes = [1, 2, 5, 10, 50, 100, 500, 1000]
# print(block_sizes)

totals = len(block_sizes) * len(r_sizes) * len(n_sizes)

counter = 0
for block_size in block_sizes:
    for r_size in r_sizes:
        for n_size in n_sizes:
            # print(block_size, r_size, n_size)
            # <block_size> <r_size> <n_size>
            cli = "./sba.sh %d %d %d" %(block_size, r_size, n_size)
            print(cli)
            print("%.1f%% | block_size: %d, r_size: %d, n_size: %d" % (((counter / totals) * 100), block_size, r_size, n_size))
            subprocess.run("ping 127.0.0.1 -c 1", shell=True)
            time.sleep(SUBMISSION_DELAY)
            counter += 1
            pass




