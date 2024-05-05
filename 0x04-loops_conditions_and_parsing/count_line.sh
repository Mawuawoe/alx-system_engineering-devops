#!/usr/bin/env bash
echo -n "Please enter a filename: "
read -r filename
nlines=$(wc -l < "$filename")

echo "There are $nlines in $filename"
