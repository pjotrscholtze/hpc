#!/bin/python3


import sys
from glob import glob

block_size = 64
r_size = 10
n_size = 10
if len(sys.argv) > 3:
    block_size = sys.argv[1]
    r_size = sys.argv[2]
    n_size = sys.argv[3]
else:
    print(sys.argv)
    print("arguments: <block_size> <r_size> <n_size>")
    exit(1)

assignment_content = ""
with open("assignment.c", "r") as f:
    lines = f.readlines()

    out = []
    for line in lines:
        if line.startswith("#define BLOCK_SIZE "):
            line = "#define BLOCK_SIZE " + str(block_size) + "\n"
        if line.startswith("#define R_MULTIPLIER "):
            line = "#define R_MULTIPLIER " + str(r_size) + "\n"
        if line.startswith("#define SIZE_N "):
            line = "#define SIZE_N " + str(n_size) + "\n"
        out.append(line)
    assignment_content = "".join(out)

with open("assignment.c", "w") as f:
    f.writelines([assignment_content])

defines = []
with open("assignment.c", "r") as f:
    for line in f.readlines():
        if line.startswith("#define "):
            defines.append(line)

def update_sb(number: int):
    res = []
    with open("sb" + str(number)+".sh","r") as f:
        lines = []

        define_content = ""
        for define in defines:
            define_content+="echo \"%s\"\n" % define.strip()

        placed_replaceme = False
        for line in f.readlines():
            if line.startswith("echo \"#define"):
                if placed_replaceme:
                   continue
                line = define_content
                placed_replaceme = True
            lines.append(line)


        res = lines
    with open("sb" + str(number)+".sh", "w") as f:
        f.writelines(res)


# Update all sbN files where N is a number.
for file in glob("sb*.sh"):
    if file == "sba.sh": continue

    update_sb(file.split(".")[0][2:])
