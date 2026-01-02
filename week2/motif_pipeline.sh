#!/bin/bash
# 253rbif100 week2 assignment - beginning Bash scripting
# Name: Helena Balbat
# Task: motif counting and sequence extracting of R. bifella



# STEP 1: Setup

# NOTE: already created week2 directory & copied input files from /home/rbif/week2/
# Code Used (see below):
# cd ~
# mkdir week2
# cp /home/rbif/week2/* .
# ls
# NOTE: the last two lines copy everything from class input folder to personal week2 folder, and check to see they're present

# changed permissions in terminal so I can edit and execute, and all others can read and execute
# Code Used (see below):
# chmod 755 motif_pipeline.sh

# make motifs/ directory in week2 directory for later
# -p allows for creating a full directory path if it doesn't exist, but causes no issues if it already does
mkdir -p motifs 


# STEP 2: Motif Counting

# create the empty output file motif_count.txt
> motif_count.txt

# loop through all motifs
while read motif; do
   # count occurrences of the motif in the genome
   count=$(grep -o "$motif" r_bifella.fasta | wc -l)

   # write both the motif and count to output file motif_count.txt
   echo -e "$motif\t$count" >> motif_count.txt
done < interesting_motifs.txt

# message to show that step 2 completed successfully
echo "Motif counting results have been saved to motif_count.txt"


# STEP 3: Sequence Extraction
# loop over each motif
while read motif; do
    # create output file for the motif (names each file after the motif)
    outputfile="motifs/${motif}.fasta"

    # empty the file if it exists
    > "$outputfile"

    # initialize variables to hold header and sequence
    header=""
    sequence=""

    # read gene file line by line
    while read line; do
        if [[ $line == ">"* ]]; then
            # if previous sequence exists, check if it contains the motif
            if [[ -n $seq ]] && [[ $seq == *"$motif"* ]]; then
                echo "$header" >> "$outputfile"
                echo "$seq" >> "$outputfile"
            fi
            # NOTE: line 59 detects header line, line 61 checks if accumulated sequence contains the motif

            # start new sequence
            header="$line"
            seq=""
        
        else
            # append line to the current sequence
            seq="$seq$line"
        fi
    done < r_bifella.fasta
    # NOTE: 'fi' is closing statement for if blocks

    # check the last sequence in the file
    # follow same as previous previous sequences, ensures it is not missed
    if [[ -n $seq ]] && [[ $seq == *"$motif"* ]]; then
        echo "$header" >> "$outputfile"
        echo "$seq" >> "$outputfile"
    fi

done < interesting_motifs.txt

# message to show that step 3 completed successfully
echo "Sequence extraction has completed and appropriate .FASTA files have been saved to week2/motifs/"


# BONUS
# find the highest frequency motif with sort and head
# sort -k2 -nr : sorts numerically (-n) in reverse order (-r) by counts column
# head -n 1 : gets top line
# awk print $1 and $2 (variables 1 and 2) to extract motif and count
max_motif=$(sort -k2 -nr motif_count.txt | head -n 1 | awk '{print $1}')
max_count=$(sort -k2 -nr motif_count.txt | head -n 1 | awk '{print $2}')

# print output of motif with highest frequency
echo "Motif with highest frequency: $max_motif ($max_count occurrences)"

# total unique genes containing at least one motif
# grep ">" motifs/*.fasta : grabs all FASTA headers from each motif file
# sort | uniq : removes any duplicates
# wc -l : counts number of unique lines
all_headers=$(grep ">" motifs/*.fasta | sort | uniq)
total_genes=$(echo "$all_headers" | wc -l)

# print output of total number of unique genes containing at least one motif
echo "Total number of unique genes containing at least one motif: $total_genes"