#!/bin/python3
import glob
import subprocess
import json
import os
import random

def generate_key(length):
    return " ".join([str(random.randint(0,0xFF)) for i in range(length)])

results = {}
files = glob.glob("*.data")
key_sizes = range(0, 10)

for k, file in enumerate(files):
    results[file] = {}
    os.rename(file, "original.data")
    for i in key_sizes:
        key_size = 1 << i
        key_size = key_size - 1
        ratio = ((k * len(key_sizes)) + i) / (len(files) * len(key_sizes))
        print("[%.1f%s] Testing key size %d on file %s" % (ratio * 100, '%', key_size, file))
        key = generate_key(key_size)

        cmd_line = "./encrypt %s" % key
        results[file][key_size] = {
            "key": key,
            "result": subprocess.getoutput(cmd_line)
        }
    os.rename("original.data", file)


with open("results.json", "w") as f:
    f.writelines([json.dumps(results)])
