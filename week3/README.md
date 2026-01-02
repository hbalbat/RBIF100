# Bash to Python - Motif Finder Conversion (253RBIF-100)

## Code Purpose
Create two scripts (one in Bash, one in Python) that perform the same task. This task is to accept a DNA motif as an argument (such as "ATGCGT") and count how many lines in a FASTA file (sequences.fasta) contain that exact motif. By creating scripts that perform the same task, we can see the differences in the two languages and observe their strengths and practical uses. 

## How to Run
### To run in Bash:
1. In class remote-SSH terminal, make sure you are in the correct directory using:
```cd /home/balbh/week3
```
2. Run script by entering the following in the terminal (NOTE: change motif as desired):
``` ./motif_finder.sh ATGCGT sequences.fasta
```
The above works to run with just ./motif_finder.sh because the Bash script contains the shebang to run with Bash automatically.

### To run in Python3 (NOTE: must be in Python3, most recent version to accommodate -f in final print command, noted in script):
1. In class remote-SSH terminal, make sure you are in the correct directory using:
```cd /home/balbh/week3
```
2. Run script by entering the following in the terminal (NOTE: change motif as desired):
```python3 motif_finder.py ATGCGT sequences.fasta
```

## What's Included
- 'sequences.fasta' : FASTA file provided to parse through
- 'motif_finder.sh' : Bash script that accepts any motif and FASTA file as an argument, then parses through the file and counts the number of lines that contain said unique motif
- 'motif_finder.py; : converted Bash script that accomplishes the same task but in Python3

## Reflection
In terms of this particular exercise, Bash was easier for me to use. It required fewer lines of code. Bash is helpful for simple, but long, repetitive tasks. In our case, parsing through an entire FASTA file and counting the lines that contain a motif is simple. However, FASTA files are long. Bash was able to complete the task in one line of code, aside from creating two variables and then printing a final result statement. Python was still helpful, but I personally find it better for analysis due to its extensive libraries.

Fortunately, I have had experience working with Python before, so I did not have too much trouble writing the Python script to perform the same task. My only challenge that I ran into was with Visual Studio Code. I typically work with Python3, which gives us access to -f, so we can incorporate integers/variables directly into a string without having to concatenate. I have never used Visual Studio Code before, so I was confused about what was wrong (I was not aware my script was running on Python 2.7.18). I did have to consult ChatGPT to research that line of code, as my terminal was highlighting that line of code having a syntax error. It gave me a few possible reasons for error, and I was fortunately able to figure it out. It is something that can just be resolved as you run it in the terminal (typing python3 instead of just python). Other than this, I did not refer to AI for anything, just accessed our class resources.

Given what I know now, I still prefer to use Python, at least for more complex bioinformatics scripting. I can see where/when Bash could be beneficial, so I am looking forward to applying that in the future. I personally am most well-versed in exploratory data analysis, and I appreciate all the tools and libraries Python has to offer when working in that area.