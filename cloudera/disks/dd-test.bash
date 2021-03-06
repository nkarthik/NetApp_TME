#!/bin/bash

BLOCK_SIZE=$1
COUNT=$2

if [ $# != 2 ]; then
    echo "Enter the block size and count value for dd write tests."
    exit
fi

# Write test
sudo dd if=/dev/zero of=/mnt/disk1/dd-test.dat bs="$BLOCK_SIZE"k count=$COUNT conv=fdatasync

# Clear the cache
echo 3 | sudo tee /proc/sys/vm/drop_caches

# Read test
sudo dd if=/mnt/disk1/dd-test.dat of=/dev/null bs=$BLOCK_SIZE
