#!/usr/bin/env python3
# RBIF100 Week 6 - Querying Biological Databases
# Name: Helena Balbat

# Task: using RESTful APIs, extract valuable genetic information about MC1R from mygene.info and Ensembl and find homologous genes in other species
    # Step 1 - retrieve the Ensembl ID
    # Step 2 - retrieve and anaylze sequence data
    # Step 3 - identify homologous genes

# import necessary tools/packages (requests for REST APIs, Biopython)
import requests
from Bio.Seq import Seq


# STEP 1
# starting from gene name, use mygene.info RESTful API to identify corresponding human Ensembl gene ID

url = "http://mygene.info/v3/query"     # url provided by mygene.info site

# set dictionary of parameters for ensembl gene
# query = MC1R, species = human, field = ensembl.gene
parameters = {
    "q": "MC1R",
    "species": "human",
    "fields": "ensembl.gene"
}

# send request to mygene.info to get ID
response = requests.get(url, params=parameters)     # send HTTP GET request to mygene.info API with our parameters
data = response.json()      # convert returned JSON text (from request) to Python dictionary

# extract ensembl ID from returned data
# "hits" : list of search results, [0] take first (best) match 
# ensembl - access Ensembl ID section and "gene" to extract Ensembl gene ID string
ensembl_id = data["hits"][0]["ensembl"]["gene"]     
print("Ensembl ID:", ensembl_id)    # print the retrieved and stored Ensembl ID to show code worked correctly



# STEP 2
# using Ensembl database and its RESTful API, retrieve full nucleotide sequence for MC1R gene using human Ensembl gene ID
# write DNA sequence to FASTA file mc1r_sequence.fasta
# identify longest open reading frame (ORF) in retrieved DNA sequence
# use Biopython (from Bio.Seq import Seq) to translate longest ORF nucleotide sequence into corresponding amino acid sequence
# append amino acid sequence to same FASTA file

headers = {"Content-Type": "text/plain"}    # set key headers to retrieve human DNA sequence from Ensembl

# same process as step one, but send request to Ensembl REST API
ensembl_url = f"https://rest.ensembl.org/sequence/id/{ensembl_id}"    # format string literal (f) to put variable directly into url
response = requests.get(ensembl_url, headers=headers)
dna_seq = response.text

# write DNA to FASTA ("w" write mode)
with open("mc1r_sequence.fasta", "w") as f:
    f.write(">MC1R_human_genomic_DNA\n")    # write FASTA header description line
    f.write(dna_seq + "\n")      # on new line \n write full MC1R DNA sequence

# define function find_longest_orf and pass seq 
def find_longest_orf(seq):
    seq = seq.upper()
    stop_codons = {"TAA", "TAG", "TGA"}
    longest_orf = ""    # store empty list for loop

    # range three for every codon reading frame
    for frame in range(3):
        for i in range(frame, len(seq) - 2,3):    # start at position frame, move forward three bases at a time through entire sequence, but stop before there are no more complete codons
            codon = seq[i:i+3]      # extract start codon
            if codon == "ATG":      # recognizes start codon ATG
                for j in range(i, len(seq) - 2, 3):     # stays in the outer frame but look ahead codon-by-codon until you reach a stop
                    stop = seq[j:j+3]   # extract stop codon
                    if stop in stop_codons:
                        orf = seq[i:j]      # once reached a stop, ORF runs from i to j
                        if len(orf) > len(longest_orf):     # compare new ORF to previously stored ORF, store bigger one to return 
                            longest_orf = orf
                        break

    # return final result
    return longest_orf

# translate ORF to amino acid sequence with Biopython
longest_orf = find_longest_orf(dna_seq)
protein_seq = Seq(longest_orf).translate(to_stop=True)

# append amino acid sequence to FASTA file mc1r_sequence.fasta
with open("mc1r_sequence.fasta", "a") as f:
    f.write(">MC1R_longest_ORF_protein\n")
    f.write(str(protein_seq) + "\n") 



# STEP 3
# using Ensembl API, identify other species that contain genes homologous to human MC1R
# write the unique list of species names into a text file named mc1r_homology_list.txt

headers = {"Accept": "application/json"}      # set headers for next request

# url set with Ensembl ID, search for homo sapiens orthologues
homology_url = f"https://rest.ensembl.org/homology/id/homo_sapiens/{ensembl_id}?type=orthologues;format=condensed"

# send request to url and store JSON response in Python format
response = requests.get(homology_url, headers=headers)
homology_data = response.json()

species = set()     # new set object to store species

# for every entry in returned data, find orthologue (species) and store in empty set species
for entry in homology_data.get("data", []):
    for hom in entry.get("homologies", []):
        species.add(hom["species"])

# write species to file mc1r_homology_list.txt
with open("mc1r_homology_list.txt", "w") as f:
    for sp in sorted(species):
        f.write(sp + "\n")