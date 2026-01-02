# Motif Pipeline - Beginning Bash Scripting 253RBIF-100

## Goal
This script (titled 'motif_pipeline.sh') automates the process of counting motifs in the R. bifella genome. It creates a text file with all motif counts, as well as FASTA files for each unique motif. These FASTA files include all instances of genes that contain the unique motif. It can be used for various genome files and motif lists.

## Input Files
- 'interesting_motifs.txt' : a list of nucleotide motifs (one per line) to search for in the FASTA file.
- 'r_bifella.fasta' : selected genome sequence in FASTA format.

## Output Files
- 'motif_count.txt' : a file listing each unique motif and the number of times it occurs in the parsed genome.
- 'motifs/' directory : contains one FASTA file for each unique motif with all sequences containing that motif.

## How to Run
1. In class remote-SSH terminal, execute by typing:
```/home/balbh/week2/motif_pipeline.sh
```


## Reflection
By using loops and relative paths in this Bash script, I created a highly reusable and generalizable script that can use any motif or FASTA file. Relative paths also ensure that the script can be run regardless of the user's current directory. Using loops/conditionals allowed me to save time and condensed the code, parsing over the entire files without having to write new blocks of code for each motif.

One challenge I encountered was during the creation of my motifs/ directory. It fortunately had a simple fix, but I tried to solve one issue and created another. Since we want to use relative paths, I wanted to make sure that I included 'cd ~/week2' in my script at the beginning. At another part of my script, I had the code 'mkdir -p week2/motifs' to make that directory under week2. However, since I already had that directory created, and then had the cd code added to the beginning, it parsed through all of my motifs in step 3 but said there was no such file or directory. I realized that I had accidentally created a separate folder entirely, also under week2, that was called week2/motifs. I edited my code to 'mkdir -p motifs' and removed the extra directory I created, so that solved my problem. It is sometimes frustrating that even little mistakes can completely mess up a script. I have had similar issues in Python before, but I find Python to be a little more forgiving.

In bioinformatics workflows, it is important to avoid hardcoding and instead write flexible/reusable scripts. This is helpful for many reasons, notably because you will often need to apply code in multiple scenarios, whether that be using different files, changing small pieces of code, or simply just needing to be in different directories. It is much easier to write a base code that can be reused in various ways, making small changes as needed or even just feeding it different inputs. For example, I could use my script to parse the genome and count motifs in the S. cerevisiae genome or even the H. sapiens genome if I wanted to. I would simply need to download their respective FASTA files and input those files instead of r_bifella.fasta. By keeping the same flexible code, it also reduces the risk of errors you would create by rewriting the same code 10 or more times.



## AI USE DISCLOSURE
I did use the help of ChatGPT for parts of this assignment, solely for help in debugging when I got stuck and for explaining concepts in different ways than we got in this week's readings. There were certain issues I ran into, like the one I explained above, so I was able to ask what I might have done wrong in suspected areas of broken code. Whenever I did utilize ChatGPT, I would check after any output it gave me by testing it in my own environment and by researching further online. I stuck primarily to using our class resources for this assignment. If ChatGPT provided a piece of code for me, I asked it to explain exactly what it meant so I knew what I would be fixing in my code. I then put notes into my code to explain what each line was for, both for myself and anyone using my script.