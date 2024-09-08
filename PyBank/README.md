# Financial Analysis Script
## Overview
This Python script is designed to analyze financial data from a CSV file and generate a report. The script calculates the total number of months, the total profit/loss, the average change in profit/loss, and identifies the greatest increase and decrease in profits over the entire period.

## File Structure
- Script Directory:
  - The script is intended to run in the context of a project directory, specifically under the PyBank challenge of a Python learning project.
- Directories:
  - Resources: Contains the input data file budget_data.csv.
   - Analysis: Stores the output analysis report as financial_analysis.txt.

## Script Explanation
1, Importing Modules:
- The script uses the os and csv modules. os is used for file path operations and creating directories, and csv is used for reading the CSV data.
2. Setting Up Paths:
- The base directory for the input file and the output directory are specified using absolute paths.
- The script ensures that the output directory exists by using os.makedirs() with exist_ok=True.
3. Reading the CSV File:
- The script opens the budget_data.csv file and reads its contents.
- It skips the header row using next(csv_data).
4. Processing Data:
- The script iterates through each row to calculate:
 - total_months: The total number of months recorded in the dataset.
 - total_profit_loss: The cumulative profit/loss over the entire period.
 - monthly_changes: The changes in profit/loss from month to month.
 - gi: The greatest increase in profits.
 - gd: The greatest decrease in profits.
5. Calculating Averages:
- After processing all rows, the script calculates the average change in profit/loss across the months.
6. Generating the Output:
- The results are formatted into a report string that is printed to the console and saved to financial_analysis.txt in the Analysis directory.
## Usage
1. Run the Script:
- Execute the script using Python in git bash: <pre>
python financial_analysis.py</pre> 
- Ensure that the input file budget_data.csv is in the Resources directory before running the script.
2. View the Results:
- After execution, the results will be printed to the console.
- The detailed financial analysis will be saved to financial_analysis.txt in the Analysis directory.
## Output Example
The output of the script will look like this:
<pre>
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)</pre>
## References
Class slides and activities
<pre>file:///C:/Users/amrit/Downloads/aus_3.1_Introduction_to_Python.pdf</pre>
<pre>file:///C:/Users/amrit/Downloads/aus_3.3_Deeper_Dive_into_Python.pdf</pre>
<pre>https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository</pre>
<pre>https://www.google.com/search?q=how+to+delete+folder+uding+git+bash&rlz=1C1CHBF_en-GBAU886AU886&oq=how+to+delete+folder+uding+git+bash&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMggIAhAAGBYYHjIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjINCAYQABiGAxiABB</pre>
<pre>file:///C:/Users/amrit/Downloads/aus_3.1_Introduction_to_Python.pdf</pre>


