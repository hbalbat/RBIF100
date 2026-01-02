#!/bin/bash
# 253rbif100 wee32 assignment - motif finder
# Name: Helena Balbat
# Task: top motifs per exome - for each FASTA in exomesCohort/ determine 3 most frequent motifs using motif_list.txt, output only sequences (w/ headers) that contain >= 1 of those to new FASTA files 

input_directory="exomesCohort"
motif_file="/home/rbif/week4/motif_list.txt"
output_directory="topmotifs"

# loop through all FASTA files in exomesCohort/
for fasta in "$input_directory"/*.fasta; do
    exome_name=$(basename "$fasta" .fasta)
    echo "Processing $exome_name"

    # count motif occurrences
    declare -A motif_counts
    while read motif; do
        count=$(grep -o "$motif" "$fasta" | wc -l)
        motif_counts["$motif"]=$count
    done < "$motif_file"

    # get the top 3 motifs
    top_motifs=$(for m in "${!motif_counts[@]}"; do
        echo "${motif_counts[$m]} $m"
    done | sort -nr | head -n 3 | awk '{print $2}')

    # print top motifs
    echo "  Top motifs: $top_motifs"

    # convert the top motifs to an array
    read -ra motifs_array <<< "$top_motifs"

    # output all sequences containing at least 1 top motif
    output_file="$output_directory/${exome_name}_topmotifs.fasta"
    > "$output_file"

    # header and seq - store current header for the loop, the reset the sequence for accumulation (collect top 3)
    header=""
    seq=""
    # read through FASTA line by line to check for motifs
    while read -r line; do
        if [[ $line == ">"* ]]; then
            # process the previous sequence
            if [[ -n $seq ]]; then
                for motif in "${motifs_array[@]}"; do
                    # NOTE: * on both sides checks for matches anywhere in the sequence (wildcard)
                    if [[ $seq == *$motif* ]]; then
                        echo "$header" >> "$output_file"
                        echo "$seq" >> "$output_file"
                        break
                    fi
                done
            fi
            header="$line"
            seq=""
        else
            seq+="$line"
        fi
    done < "$fasta"

    # handle the last sequence (ensures sequence is written if it is top motif)
    if [[ -n $seq ]]; then
        for motif in "${motifs_array[@]}"; do
            if [[ $seq == *$motif* ]]; then
                echo "$header" >> "$output_file"
                echo "$seq" >> "$output_file"
                break
            fi
        done
    fi

    # show that new FASTA file was written
    echo "  Written $output_file"
done