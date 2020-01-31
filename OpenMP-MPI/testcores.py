#!/usr/bin/python3

import subprocess
import time

commands = [
    {
        "name": "4 cores",
        "cmd": "mpirun -np 4 ./assignment",
        "timeout": 4,
    },
    {
        "name": "3 cores",
        "cmd": "mpirun -np 3 ./assignment",
        "timeout": 3,
    },
    {
        "name": "2 cores",
        "cmd": "mpirun -np 2 ./assignment",
        "timeout": 2,
    },
    {
        "name": "1 cores",
        "cmd": "mpirun -np 1 ./assignment",
        "timeout": 1,
    },
]


def run_for_seconds(cmd: str, timeout: float):
    p = subprocess.Popen(cmd, shell=True)
    time.sleep(timeout)
    p.kill()



for item in commands:
    print(">>> [START] Starting '" + item["name"] + "' timeout: " + str(item["timeout"]))
    run_for_seconds(item["cmd"], item["timeout"])
    print(">>> [STOP] Stoping '" + item["name"] + "' timeout: " + str(item["timeout"]))
