#!/bin/bash
# 253rbif100 wee32 assignment - motif finder
# Name: Helena Balbat
# Task: perform an edit - for each {exomename}_precirspr.fasta, insert letter A before NGG site and save to {exomename}_postcrispr.fasta files

# set input and output directories
input_directory="precrispr"
output_directory="postcrispr"

# loop through all files in precrispr directory
for fasta in "$input_directory"/*_precrispr.fasta; do
    exome_name=$(basename "$fasta" _precrispr.fasta)
    # set new file name for all edited sequences
    output_file="$output_directory/${exome_name}_postcrispr.fasta"
    # print that name has been edited
    echo "Editing $exome_name"

    # RS=">" : treat FASTA entry as a record to store
    # ORS="" : output record separator (store all outputs separately to put in postcrispr)
    # NOTE: for(i=2;i<=length(lines);i++) line 27, looping over all lines after header line 1, concatenate them all into one string (seq) to read through continuously
    # line 28 makes substitution - "\\1A\\2" targets everything before GG (\1), inserts an A before the GG site, and the GG itself (\2)
    awk 'BEGIN{RS=">"; ORS=""}
    NR>1 {
        split($0, lines, "\n")
        header=lines[1]
        seq=""
        for(i=2;i<=length(lines);i++) seq=seq lines[i]
        gsub(/(.*)(GG)/, "\\1A\\2", seq)
        print ">" header "\n" seq "\n"
    }' "$fasta" > "$output_file"

    # print that new FASTA file has been written
    echo "  Written $output_file"
done