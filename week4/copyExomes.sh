#!/bin/bash
# 253rbif100 wee32 assignment - motif finder
# Name: Helena Balbat
# Task: cohort selection - parse clinical_data.txt, select samples with diameter between 20-30mm (inclusive) that have genomes sequenced, copy into new directory exomesCohort/

# set variables as files from class directory to parse through, output folder
clinical="/home/rbif/week4/clinical_data.txt"
input_exomes="/home/rbif/week4/exomes"
output_directory="exomesCohort"

# -F '\t' uses tab as field separator (tab-delimited file)
# NOTE: NR>1 (number of record skips the first line, header row - this is due to how file is formatted)
# column $3 = diameter, $5 = status (sequenced/not sequenced), $6 = sample code
# gsub removes spaces so nothing interferes with comparisons
# search for files with d>= 20 and d <= 30 that are also genome sequenced
# print sample code for use in loop, store each file to send to exomesCohort directory
awk -F '\t' 'NR>1 {
    d=$3
    status=$5
    code=$6
    gsub(/ /,"",d)
    gsub(/ /,"",status)
    gsub(/ /,"",code)
    status=tolower(status)
    if(d>=20 && d<=30 && status=="sequenced") print code
}' "$clinical" |
while read sample
do
    fasta_path="$input_exomes/${sample}.fasta"
    if [[ -f "$fasta_path" ]]; then
        echo "Copying $sample.fasta"
        cp "$fasta_path" "$output_directory/"
    else
        echo "Warning: FASTA not found for $sample"
    fi
done