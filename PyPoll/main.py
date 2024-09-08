import os
import csv

# File paths
election_data = os.path.join(r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyPoll\Resources\election_data.csv")
output_file = os.path.join(r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyPoll\Analysis", "election_results.txt")

# Initialize variables
TotalVotes = 0
candidateVotes = {}

# Read the CSV file
with open(election_data, 'r') as csv_file:
    poll_data = csv.reader(csv_file, delimiter=",")
    
    # Read the header
    csv_header = next(poll_data)
    
    # Process each row
    for row in poll_data:
        TotalVotes += 1
        candi = row[2]
        
        if candi in candidateVotes:
            candidateVotes[candi] += 1
        else:
            candidateVotes[candi] = 1

# Determine the winner
winner = max(candidateVotes, key=candidateVotes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")
for candi, votes in candidateVotes.items():
    percentage = (votes / TotalVotes) * 100
    print(f"{candi}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
with open(output_file, 'w') as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {TotalVotes}\n")
    txt_file.write("-------------------------\n")
    for candi, votes in candidateVotes.items():
        percentage = (votes / TotalVotes) * 100
        txt_file.write(f"{candi}: {percentage:.3f}% ({votes})\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-------------------------\n")