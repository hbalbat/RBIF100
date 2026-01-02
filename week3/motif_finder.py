# 253rbif100 week3 assignment - Bash to Python
# Name: Helena Balbat
# Task: compare process of scripting in Bash and Python by converting a Bash script you've previously written into Python
# the following is the Python script portion of the assignment
# take a DNA motif as an argument and count how many lines in a FASTA file that contain the exact motif

# BONUS: Modify your Python script to provide additional summary statistics about your FASTA file, such as the total number of sequences in the file or the percentage of sequences containing the motif.

# import sys package - allows you to store motif and FASTA file directly from terminal
# no need to hard-set variables, more flexible
import sys

# create places to store variables (to use as arguments)
motif = sys.argv[1]   # selected motif to search for
file = sys.argv[2]   # selected FASTA file to parse through

# set beginning count to 0
count = 0 

# BONUS: create variable to count total sequences
total_sequences = 0

# open FASTA file and count lines that contain selected motif
with open(file, "r") as f:
    for line in f:
        line = line.strip()   # BONUS: remove whitespace/newline
        if line.startswith(">"):   # BONUS: skip header lines in the FASTA file
            continue
        total_sequences += 1   # BONUS: add one to total sequence count
        if motif in line:   # conditional to check if the motif is present
            count += 1   # add one to the count 

# print final statement
# f before the quotes and {} let us put variables in with string
print(f"The motif {motif} appears in {count} sequences.")

# BONUS: calculate percentage and print additional summary stats
if total_sequences > 0:  # avoid division by zero (only calculate when there is AT LEAST ONE motif present)
    percentage = (count / total_sequences) * 100   # set variable as percentage calculation
    print(f"Total sequences in file: {total_sequences}")
    print(f"Percentage of sequences containing the motif: {percentage:.2f}%")   # prints variable as a percentage