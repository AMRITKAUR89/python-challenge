import os
import csv

budget_data = os.path.join(r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyBank\Resources\budget_data.csv")

with open(budget_data) as csv_file:
    csv_months = csv.reader(csv_file, delimiter=",")
    
    # Skip the header
    csv_header = next(csv_months)
    print(f"Finacial Analysis")
    
    # Initialize the total months counter
    Totalmonths = 0
    
    # Iterate through each row
    for row in csv_months:
        if row[0] != "":  
            Totalmonths += 1
    
    
    print(f"Total Months: {Totalmonths}")


