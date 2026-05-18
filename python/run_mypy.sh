#!/bin/sh

for directory in $(ls -d */)
do
  cd $directory
  mypy .
  cd ../
done
