#!/bin/sh

rm -rf results
mkdir results

# Key size 1
./encrypt 1 > results/original_1.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 1 > results/10byte_1.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 1 > results/512byte_1.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 1 > results/1024byte_1.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 1 > results/10240byte_1.data
mv ./original.data  ./10240byte.data

# Key size 2
./encrypt 2 > results/original_2.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 2 > results/10byte_2.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 2 > results/512byte_2.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 2 > results/1024byte_2.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 2 > results/10240byte_2.data
mv ./original.data  ./10240byte.data

# Key size 4
./encrypt 4 > results/original_4.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 4 > results/10byte_4.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 4 > results/512byte_4.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 4 > results/1024byte_4.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 4 > results/10240byte_4.data
mv ./original.data  ./10240byte.data

# Key size 8
./encrypt 8 > results/original_8.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 8 > results/10byte_8.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 8 > results/512byte_8.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 8 > results/1024byte_8.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 8 > results/10240byte_8.data
mv ./original.data  ./10240byte.data

# Key size 16
./encrypt 16 > results/original_16.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 16 > results/10byte_16.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 16 > results/512byte_16.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 16 > results/1024byte_16.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 16 > results/10240byte_16.data
mv ./original.data  ./10240byte.data

# Key size 32
./encrypt 32 > results/original_32.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 32 > results/10byte_32.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 32 > results/512byte_32.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 32 > results/1024byte_32.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 32 > results/10240byte_32.data
mv ./original.data  ./10240byte.data

# Key size 32
./encrypt 32 > results/original_32.data
mv ./original.data ./original.data.bak

mv ./10byte.data ./original.data
./encrypt 32 > results/10byte_32.data
mv ./original.data  ./10byte.data

mv ./512byte.data ./original.data
./encrypt 32 > results/512byte_32.data
mv ./original.data  ./512byte.data

mv ./1024byte.data ./original.data
./encrypt 32 > results/1024byte_32.data
mv ./original.data  ./1024byte.data

mv ./10240byte.data ./original.data
./encrypt 32 > results/10240byte_32.data
mv ./original.data  ./10240byte.data


