#!/bin/bash

set -e
# set -x


for((i=0;i<5;i++))
do
  (python test.py -n=$i -s=$i -x=2 -y=3)
done
