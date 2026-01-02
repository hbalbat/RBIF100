RBIF100 Week 5 - Building a Python Pipeline for DNA Sequence Analysis

Purpose:
This pipeline loads DNA sequence from selected FASTA file (from /home/rbif/week5/sequences.fasta) then filters sequences only longer than 100 nucleotides. 
Calculates the GC content and outputs the summary data into a CSV file.

Files Included:
dna_pipeline.py : main pipeline Python script
sequence_summary.csv : output summary CSV file

How to Run:
Type the following into the remote terminal.
cd /home/balbh/week5
python3 dna_pipeline.py

Reflection:
Similar to our previous assignment, where we broke our tasks up into individual Bash scripts, breaking our tasks up into functions this week made them more digestible. When there were errors, I could debug individual functions rather than trying to work out a ton of code blocks. It is helpful to see functions that have specific names and passed arguments so I can see exactly what is going on where. Creating the main function at the end helps to bring everything together while keeping all tasks separate and readable.
However, functions can be difficult when it comes to calling them in other functions. Sometimes, passing arguments with the correct names can be confusing as well, because they need to be explicitly written outside of the function you're passing them to (so Python can find what it needs to pass to your function). We need to make sure that results are returned & stored both properly and globally so we can access them from other points in the script. I did not encounter many notable issues as I have worked with functions and dataframes in Python before, so I have decent experience.
Bioinformatics workflows are most likely structured frequently as pipelines rather than individual scripts because it helps condense the number of files you have. Functions work similarly to scripts, but they allow you to work from one document on a single tab. Last time, I had to switch tabs multiple times to see what I was doing with each script and making sure everything was saved and working correctly. Using pipelines with functions still keeps work/tasks separate and lets you write code more easily, but saves time and space as well.

AI Use Disclosure:
There were only a few times when I approached ChatGPT to assist with this assignment. I have never used (if __name__ == "__main__":) before, and I was confused as to what I needed to do with it. I have used main() functions before, but I used AI to help further explain why the prior code would be helpful. It ensures that my main pipeline would only run when my file is executed directly, rather than when it is imported as a module. I had ChatGPT explain this to me in detail as this was new to me. I also used it to assist me with the bonus challenge, as I have had experience working with adding extra statistics to assignments. I had originally tried to include it in my dataframe, but that was not the right approach since I was only calculating summary stats for the entire dataset. I had ChatGPT help show where to include it in my create_summary() function so it would still print, but not include it in the dataframe. 