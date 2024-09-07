import os
import csv

election_data = os.path.join(r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyPoll\Resources\election_data.csv")

output_file = os.path.join(r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyPoll\Analysis")

with open(election_data,'r')as csv_file:
    poll_data = csv.reader(csv_file, delimiter=",")

    csv_header = next(poll_data)
    print("Election Results")

    TotalVotes = 0

    for row in poll_data:
        if row[0] != "":
            TotalVotes += 1
    
    print(f'Total Votes: {TotalVotes}')