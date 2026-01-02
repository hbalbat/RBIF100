#!/bin/bash
# 253rbif100 wee32 assignment - motif finder
# Name: Helena Balbat
# Task: find CRISPR candidates - for each {exomename}_topmotifs.fasta, identify sequences with at least 20 nucleotides upstream of NGG site, write candidate headers & sequences to new FASTA files

# set input and output directories 
input_directory="topmotifs"
output_directory="precrispr"

# loop through FASTA files in topmotifs
for fasta in "$input_directory"/*_topmotifs.fasta; do
    exome_name=$(basename "$fasta" _topmotifs.fasta)
    # set new file name for all CRISPR candidates
    output_file="$output_directory/${exome_name}_precrispr.fasta"
    # print that name has been edited
    echo "Processing $exome_name"

    # RS=">" : treat FASTA entry as a record to store
    # /[ATCG]{20,}GG/ matches >= 20 nucleotides upstream of NGG sequences - only store these
    awk 'BEGIN{RS=">"; ORS=""}
    NR>1 {
        split($0, lines, "\n")
        header=lines[1]
        seq=""
        for(i=2;i<=length(lines);i++) seq=seq lines[i]
        if(seq ~ /[ATCG]{20,}GG/) {
            print ">" header "\n" seq "\n"
        }
    }' "$fasta" > "$output_file"

    # print that new FASTA file (precrispr) has been created
    echo "  Written $output_file"
done