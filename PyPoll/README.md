# Election Results Analysis Script
## Overview
This Python script is designed to analyze election data from a CSV file and generate a report summarizing the results. The script calculates the total number of votes cast, the number of votes each candidate received, the percentage of votes each candidate won, and determines the winner of the election.

## File Structure
- Script Directory:
  - The script is designed to be run in the context of the PyPoll challenge within a Python learning project.
- Directories:
  - Resources: Contains the input data file election_data.csv.
  - Analysis: Stores the output analysis report as Election_results.txt.
## Script Explanation
1. Importing Modules:
  - The script uses the os and csv modules. os is used for file path operations, and csv is used for reading the CSV data.
2. Setting Up Paths:
  - The base directory for the input file and the output directory are specified using file paths.
The output file is specified as Election_results.txt within the Analysis directory.
3. Initializing Variables:
  - TotalVotes = 0: Tracks the total number of votes cast.
  - candidateVotes = {}: A dictionary to store the number of votes each candidate received.
4. Reading the CSV File:
  - The script opens the election_data.csv file and reads its contents.
  - It skips the header row using next(poll_data).
5. Processing Data:
  - The script loops through each row to:
  - Increment TotalVotes for each vote.
  - Extract the candidate's name and update their vote count in candidateVotes.
6. Determining the Winner:
  - The script identifies the candidate with the most votes using max(candidateVotes, key=candidateVotes.get).
7. Generating and Printing the Output:
  - The election results, including the total votes, each candidate's vote percentage, and total votes, are printed to the console.
  - The winner of the election is also printed.
8. Saving the Results to a Text File:
  - The script writes the results to Election_results.txt in the Analysis directory, following the same format as the console output.
## Usage
1. When we run the Script:
- Execute the script using Python:<pre>
python main.py</pre>
- Ensure that the input file election_data.csv is in the Resources directory before running the script.
2. View the Results:
- After execution, the results will be printed to the console.
- The detailed election results will be saved to Election_results.txt in the Analysis directory.
## Output Example
The output of the script will look like this:
<pre>
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
</pre>

## References
Class slides and activities
<pre>file:///C:/Users/amrit/Downloads/aus_3.1_Introduction_to_Python.pdf</pre>
<pre>file:///C:/Users/amrit/Downloads/aus_3.3_Deeper_Dive_into_Python.pdf</pre>
<pre>https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository</pre>
<pre>https://www.google.com/search?q=how+to+delete+folder+uding+git+bash&rlz=1C1CHBF_en-GBAU886AU886&oq=how+to+delete+folder+uding+git+bash&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjINCAYQABiGAxiABB</pre>
<pre>file:///C:/Users/amrit/Downloads/aus_3.1_Introduction_to_Python.pdf</pre>













