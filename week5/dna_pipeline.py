#!/usr/bin/env python3
# Name: Helena Balbat
# RBIF100 Week 5 - Building a Python Pipeline for DNA Sequence Analysis
# Task: write a Python script named dna_pipeline.py that accomplishes the following tasks clearly structured into separate reusable functions:
    # function 1: data loading 
    # function 2: sequence filtering
    # function 3: analysis
    # function 4: summary and saving results

# NOTE: pulls FASTA file from class /home/rbif/week5 directory
# NOTE: script should clearly indicate order of steps (pipeline) by calling these functions sequentially in a main function or a clearly structured code block

# import pandas library
import pandas as pd


# FUNCTION 1: Data Analysis
# create a function to read DNA sequences from a provided FASTA file into a Python data structure
# can use a list or dictionary to store data clearly

# define function load_fasta, feeding it an argument fasta_file
# reads FASTA file and returns a dictionary {seq_id: sequence}
def load_fasta(fasta_file):
    # set blank dictionary to variable sequences to hold and return at the end
    sequences = {}
    # set current_id to none (loop will update this for every sequence header)
    current_id = None

    # loop to parse through FASTA file and store sequence IDs
    with open(fasta_file, "r") as f:
        for line in f:
            line = line.strip()   # strip line of whitespaces
            if line.startswith(">"):   # identify header lines (start with >)
                current_id = line[1:]   # remove ">" so it just contains seq ID 
                sequences[current_id] = ""   # create empty string to store sequence in the dictionary sequences
            else:
                sequences[current_id] += line   # append new sequence line to whatever is stored for current_id (stores sequence for said ID)

    # return dictionary sequences to call in later functions
    return sequences



# FUNCTION 2: Sequence Filtering
# implement a function to filter sequences, keeping only sequences longer than 100 nucleotides

# define function filter_sequences, feeding it the returned seq_dictionary with a min_length=100
# returns only the sequences longer than the min_length
def filter_sequences(seq_dictionary, min_length=100):
    # return dictionary of filtered sequences for calling in later functions
    return {
        seq_id: seq   # define what the key-value pairs look like in our dictionary
        for seq_id, seq in seq_dictionary.items()   # loop through all items in dictionary
        if len(seq) > min_length   # return only those with sequences longer than the min_length of 100 (note: we could change the min_length to whatever if we wanted to)
    }



# FUNCTION 3: Analysis
# write a function to calculate the GC-content (% of nucleotides that are G or C) for each sequence

# define function calculate_gc and pass filtered sequence dictionary as argument
# return GC-content %
def calculate_gc(sequence):

    gc_count = sequence.count("G") + sequence.count("C")   # count all Gs and Cs in each sequence
    
    # return the count divided by the total length of sequence as a percent
    return (gc_count / len(sequence)) * 100 



# FUNCTION 4: Summary and Saving Results
# write a function that generates a summary table or dataframe (with pandas) showing the sequence ID, length, and GC-content for each filtered sequence
# save the summary table into a CSV file named sequence_summary.csv


# define function create_summary and pass it filtered sequences and output_csv to store summary in
# create a pandas dataframe and save as sequence_summary.csv
def create_summary(filtered_seq, output_csv="sequence_summary.csv"):
    data = []   # store sequence data as empty list for structured format

    # loop through filtered sequence dictionary
    for seq_id, seq in filtered_seq.items():
        length = len(seq)   # compute length
        gc = calculate_gc(seq)   # call earlier function to get GC value

        # add stats to data list (each iteration creates new instance, list of many dictionaries for dataframe)
        data.append({
            "Sequence ID:": seq_id,
            "Length": length,
            "GC Content": gc
        })

    # create dataframe using pandas, using stored variable data
    df = pd.DataFrame(data)
    
    # BONUS STATS
    # calculate average sequence length 
    avg_length = df["Length"].mean()
    # calculate % of sequences with GC content over 75% (high threshold of choice)
    high_gc = (df["GC Content"] > 70).sum() / len(df) * 100 

    # PRINT BONUS STATS
    print(f"Average Length: {avg_length}")
    print(f"% of sequences with GC Content ?|> 70%: {high_gc:.2f}%")

    # output dataframe to CSV file
    df.to_csv(output_csv, index=False)

    # return dataframe
    return df



# FINAL STEP: calling all functions (using a main function)
def main():
    fasta_file = "/home/rbif/week5/sequences.fasta"   # FASTA file of choice

    # step 1: load FASTA 
    sequences = load_fasta(fasta_file)

    # step 2: filter sequences
    filtered = filter_sequences(sequences)

    # steps 3 & 4: analyze sequences and save
    summary_df = create_summary(filtered)

    print("Pipeline completed. Summary has been saved to sequence_summary.csv")
    print(summary_df)

# only run function when dna_pipeline.py is executed directly
if __name__ == "__main__":
    main()