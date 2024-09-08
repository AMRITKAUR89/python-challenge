# Import Necessary Modules
<pre>
import os
import csv </pre>
# Set File Paths
<pre>
election_data = os.path.join("C:\\Users\\amrit\\LearnPython\\assignment1\\python-challenge\\PyPoll\\Resources\\election_data.csv")
output_file = os.path.join("C:\\Users\\amrit\\LearnPython\\assignment1\\python-challenge\\PyPoll\\Analysis", "Election_results.txt") </pre>
# Initialize Variables
<pre>
TotalVotes = 0
candidateVotes = {} (an empty dictionary to store the votes for each candidate) </pre>
# Read the CSV File
<pre>
Open the CSV file: with open(election_data, 'r') as csv_file
Create a CSV reader: poll_data = csv.reader(csv_file, delimiter=",")</pre>
## Skip the header row: 
<pre>csv_header = next(poll_data)</pre>
## Process Each Row in the CSV
<pre>
For each row in poll_data:</pre>
#### Increment TotalVotes by 1.
#### Extract the candidate's name:
<pre> candi = row[2] </pre>
#### If candi is already in candidateVotes, increment their vote count.
#### Otherwise, add candi to candidateVotes with an initial vote count of 1.
## Determine the Winner
#### Find the candidate with the most votes:
<pre>winner = max(candidateVotes, key=candidateVotes.get)</pre>
## Print Election Results
<pre>
Print "Election Results"
Print "-------------------------"
Print TotalVotes</pre>

#### For each candidate in candidateVotes, print their name, vote percentage, and total votes.
#### Print the winner of the election.
#### Save the Results to a Text File

## Open the output file for writing: 
<pre>with open(output_file, 'w') as txt_file</pre>
#### Write the election results to the file, following the same format as the console output.
