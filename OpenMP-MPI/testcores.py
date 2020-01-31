#!/usr/bin/python3

import subprocess
import time

commands = [
    {
        "name": "4 cores",
        "cmd": "mpirun -np 4 ./assignment",
        "timeout": 5,
    },
    {
        "name": "3 cores",
        "cmd": "mpirun -np 3 ./assignment",
        "timeout": 5,
    },
    {
        "name": "2 cores",
        "cmd": "mpirun -np 2 ./assignment",
        "timeout": 5,
    },
    {
        "name": "1 cores",
        "cmd": "mpirun -np 1 ./assignment",
        "timeout": 5,
    },
]


def run_for_seconds(cmd, timeout):
    p = subprocess.Popen(cmd, shell=True)
    time.sleep(timeout)
    p.kill()



for item in commands:
    print(">>> [START] Starting '" + item["name"] + "' timeout: " + str(item["timeout"]))
    time.sleep(0.1)
    run_for_seconds(item["cmd"], item["timeout"])
    time.sleep(0.1)
    print(">>> [STOP] Stoping '" + item["name"] + "' timeout: " + str(item["timeout"]))
