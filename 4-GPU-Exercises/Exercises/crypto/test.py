#!/bin/python3
import glob
import subprocess
import json
import os

results = {}
files = glob.glob("*.data")
key_sizes = range(0, 8)

for k, file in enumerate(files):
    results[file] = {}
    os.rename(file, "original.data")
    for i in key_sizes:
        key_size = 1 << i
        ratio = ((k * len(key_sizes)) + i) / (len(files) * len(key_sizes))
        print("[%.1f%s] Testing key size %d on file %s" % (ratio * 100, '%', key_size, file))
        cmd_line = "./encrypt %d" % key_size
        # print(cmd_line)
        results[file][key_size] = subprocess.getoutput("ping -c 2 127.0.0.1")
    os.rename("original.data", file)

# with open("results.json", "w") as f:
#     f.writelines([json.dumps(results)])
