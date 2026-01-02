#!/bin/bash
# 253rbif100 week3 assignment - Bash to Python
# Name: Helena Balbat
# Task: compare process of scripting in Bash and Python by converting a Bash script you've previously written into Python
# the following is the Bash script portion of the assignment
# take a DNA motif as an argument and count how many lines in a FASTA file that contain the exact motif

# set motif and file variables as 1 and 2, those being the first and second arguments
motif=$1
file=$2

# count the number of times the argument $motif appears in the given FASTA file $file
# parse through entire file and count how many times motif appears, store as variable $count
count=$(grep -c "$motif" "$file")

# output statement to show counted results
echo "The motif $motif appears in $count sequences."