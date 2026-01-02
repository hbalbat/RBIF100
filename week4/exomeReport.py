#!/usr/bin/env python3
# 253rbif100 wee32 assignment - motif finder
# Name: Helena Balbat
# Task: summarize cohort - text report listing, for each organism: discoverer name, diameter, code name, environment, print union of gene names observed across cohort drawn from CRISPR-ready files

# import libraries to provide functions for file paths/directories (os) and find files that match patterns in a folder (glob)
import os
import glob

# set variables with locations (files and directories)
clinical_file = "/home/rbif/week4/clinical_data.txt"
precrispr_directory = "precrispr"
report_file = "report.txt"

# read clinical data
# store cohort in blank list
cohort = []
# loop through clinical file 
with open(clinical_file) as f:
    # read first line as header
    header = f.readline()
    # loop over rest of the lines in file
    for line in f:
        # split lines by tabs and remove whitespace with line.strip
        cols = line.strip().split("\t")
        # skip any lines with missing data (doesn't contain all necessary columns)
        if len(cols) < 6:
            continue
        # write names of columns, store as cols
        discoverer, location, diameter, env, status, code = cols
        # keep only the sames with the requirements we specified for diameter and sequenced genomes
        if 20 <= float(diameter) <= 30 and status.lower() == "sequenced":
            cohort.append((discoverer, diameter, code, env))

# collect gene names from precrispr files (treat sequence IDs as gene names)
gene_names = set()
# find all files in precrispr/ that end with _precrispr.fasta
for fpath in glob.glob(os.path.join(precrispr_directory, "*_precrispr.fasta")):
    with open(fpath) as f:
        # loop through each line - if it starts with >, it is a FASTA header
        for line in f:
            if line.startswith(">"):
                # add to gene_names set to ensure no duplicate listings
                gene_names.add(line[1:].strip())

# write text report including discoverer name, diameter, code name, environment, and union of gene names observed across cohort
with open(report_file, "w") as out:
    for entry in cohort:
        out.write("\t".join(entry) + "\n")
    # sort gene names and write as a union in one final line
    out.write("Union of genes:\t" + ", ".join(sorted(gene_names)) + "\n")

# print that the report has been written
print(f"Report written to {report_file}")