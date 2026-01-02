Files & Directories in Week4:
exomesCohort/ : files copied into this folder by copyExomes.sh
precrispr/ : output folder for sequences before CRISPR editing
postcrispr/ : output folder for sequences after CRISPR editing
topmotifs/ : stores results for motif findings
copyExomes.sh : cohort selection Bash script
createCrisprReady.sh : find top motifs per exome Bash script
identifyCrisprSite.sh : find CRISPR candidates Bash script
editGenome.sh : perform CRISPR edit Bash script
exomeReport.py : cohort summary Python file
report.txt : final generated summary report

scripts will only read from /home/rbif/week4/ .txt files, never edits (use them as inputs)

NOTE: each script contains the necessary tasks and their goals


How to Run:
In remote AWS server, type each command as follows:
cd /home/balbh/week4 
bash copyExomes.sh
bash createCrisprReady.sh
bash identifyCrisprSite.sh
bash editGenome.sh
python3 exomeReport.py

These above commands ensure you first have access to my week4 folder, then you can access all files from our class week4 folder from my scripts.
Run the scripts in this order.
You can check what files were created via the Explorer window in Visual Studio Code or by using ls commands


Expected Inputs: just run the commands above, as the class week4 files are accessible directly in the scripts, and everything can be accessed within my remote week4 folder

Expected Outputs:
1. list of FASTA files in exomesCohort directory titled {exomename}.fasta
2. list of FASTA files in topmotifs directory titled {exomename}_topmotifs.fasta
3. list of FASTA files in precrispr directory titled {exomename}_precrispr.fasta
4. list of the precrispr FASTA files in the postcrispr directory titled {exomename}_postcrispr.fasta
5. final report titled report.txt generated via the exomeReport.py script

Reflection:
During this assignment, I used automation to prevent brittle code. I wanted to avoid hardcoded filenames, fixed paths, and manual steps to keep my scripts working even if input changed. For example, in my Bash scripts, I used awk to read columns automatically from our clinical_data.txt file so I did not hardcode which samples were being used. If the file added/removed samples, the code would still work. I also utilized loops to process all files and motifs without writing repetitive code. I could loop over each FASTA file to find top motifs, rather than running grep or awk on each individual file.
By splitting our workflow into multiple small scripts and one Python report, it helped with debugging and clarity. Each script handles one task, rather than one or two big scripts handling every task. If something went wrong in one script, the possible errors were much easier to find. It also allowed me to run single scripts rather than a whole pipeline, so if one step wasn't working, I only had to debug the broken script, rather than run the entire pipeline again. As for the Python report, using Python for only this section of the assignment helped to clean up text parsing. Python better handles structured data (like in clinical_data.txt), so using Python to generate a summary report was the better choice.
Again, like we've seen in previous assignments, Bash is better with quick text processing and immediate file/directory manipulation. However, handling structured data like tables and multi-line sequences is a bit harder. It can be harder to debug as it can get lengthy and confusing. This is when Python can be helpful, as Python handles structured data (tables, lists, dictionaries, etc.) very well, and you can write reusable functions more easily. However, Python is slower when it comes to large text streams. We often need to write loops and manage files that Bash can do more seamlessly. It is interesting how we can leverage the strengths of both and incorporate them into one assignment.

AI Use Disclosure:
I did utilize ChatGPT during this assignment to help with formatting/syntax, specifically with Bash. Using the awk loops, I needed to parse through all the exomes and other generated files to store selected data. For example, I was having some trouble with the tab-delimited files and reading through the columns of the file, then translating that to an awk command. I used ChatGPT to help me figure out where I was going wrong with removing whitespaces and setting variables like the diameter and genome sequencing status in copyExomes.sh. There were some other syntax errors I encountered since I am still new as a Bash learner, so I had ChatGPT look through my output errors and give some possibilities as to what was incorrect. To verify its output, I always made sure to copy my previous code to save it, but from there, I tested different changes to see what exactly I needed to fix.