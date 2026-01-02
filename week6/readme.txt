RBIF100 Week 6 - Querying Biological Databases
Name: Helena Balbat

Purpose:
Create a Python script that queries bioinformatics databases using RESTful APIs. This script explores the MC1R gene. It retrieves genetic data from public biological databases and handles biological data formats like FASTA.
The Python script contains explanations of each step. Overall, this assignment gave us practice learning how to use RESTful APIs and practice using them and JSON through requests.


Included Files:
mc1r_homology_list.txt : text file of all identified homologs to human MC1R gene
mc1r_query.py : main Python script
mc1r_sequence.fasta : FASTA file containing the MC1R longest ORF nucleotide sequence and its coordinating amino acid sequence


How to Run:
In remote class server, type the following:
cd /home/balbh/week6
python3 mc1r_query.py

This will print the Ensembl ID and output all information to the correct files.


Reflection & AI Use Disclosure:
In this assignment, I learned the basics of working with RESTful APIs. I did not know about them in the past (I have heard of APIs before, but it is new to me). I learned about how powerful even simple requests can be, allowing us to access entire genetic and other biologic databases with a single request command. I have used both UniProt and NCBI before, but I have never used Ensembl. I explored both the mygene.info and Ensembl webpages to try and learn more about what I was actually working with. I also learned how to extract this JSON return data and put it into a workable Python format, which I found interesting.
I had a very tough time working through the third part of this assignment, both with getting the code blocks to run through without error, and then getting species to actually output to the file I made. I originally kept running into errors with the URL. I was using the f/ format so I could include the Ensembl ID variable in the URL. However, I was getting TypeErrors and the webpage kept coming back as a 404 message. I was very confused, so I did consult ChatGPT here to help figure out the problem. 
To make sure I did not further break my code, and to debug individual pieces, I made a test script in my week 6 directory and tried changing the method of making the API request. I ended up setting the headers to "accept" and including the type= and format= in the URL, which solved that issue. From there, the code was running without any noticeable errors, but no species were being output into the .txt file. I figured it was an issue with the URL, but I was not 100% sure, so I did use ChatGPT to help debug this as well. It suggested I print the JSON response eventually, and it was printing orthologues, but there was a singular part in my final for loop that I needed to change. For species.add(hom["species"]), I originally had written "target" in another set of brackets, but it was not in the JSON, so it couldn't find anything.
When it came to complex debugging, particularly with JSON and RESTful API work that I am new to, consulting ChatGPT and class online resources did help me solve the issues with my code. I always made sure to test every suggestion separately and to corroborate what I found with other resources. 
I have personally done work with accessing major biological databases and sequence manipulation in a prior computational biology class, but I have not practiced much with programatically accessing them. I know how powerful these databases can be on their own (with the sheer amount of information), as well as how many possibilities there are with Python through all of its libraries. I personally love working with huge databases, and I always find it fascinating to find similarities in genetic sequences of vastly different species. I have always done this manually, but with this assignment, I can find hundreds of species within just a few commands and a little bit of time/debugging. Even working with 20 species was challenging when I had to compare them manually - I see how much more I can tackle with programmatic access!