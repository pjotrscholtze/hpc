#!/usr/bin/python3

import subprocess
import time
import datetime
import sys

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
    process = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    start_time = datetime.datetime.now().timestamp()

    while True:
        out = process.stdout.read(1)
        if out == '': 
            if process.poll() != None:
                break
        if out != '':
            sys.stdout.write(out.decode("utf-8"))
            sys.stdout.flush()
        if out.decode("utf-8") == '\n':
            if datetime.datetime.now().timestamp() - start_time > timeout:
                break
    process.kill()



for item in commands:
    print(">>> [START] Starting '" + item["name"] + "' timeout: " + str(item["timeout"]))
    time.sleep(0.1)
    run_for_seconds(item["cmd"], item["timeout"])
    time.sleep(0.1)
    print(">>> [STOP] Stoping '" + item["name"] + "' timeout: " + str(item["timeout"]))
