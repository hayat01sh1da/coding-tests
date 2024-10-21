#!/bin/sh

for directory in $(ls -d */)
do
  cd $directory
  for unittest in $(find . -name test_*.py -type f)
  do
    python $unittest
  done
  cd ../
done
