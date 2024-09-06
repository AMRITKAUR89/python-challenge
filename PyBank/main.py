import os
import csv

base_dir = r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyBank\Resources"
file_name = "budget_data.csv"

output_dir = r"C:\Users\amrit\LearnPython\assignment1\python-challenge\PyBank\Analysis"
os.makedirs(output_dir, exist_ok=True)


budget_data = os.path.join(base_dir, file_name)

with open(budget_data, 'r') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    
    csv_header = next(csv_data)
    print("Financial Analysis")
    
    total_months = 0
    total_profit_loss = 0
   
    monthly_changes = []
    previous_value = None
    gi = {"month": None, "amount": float('-inf')}
    gd = {"month": None, "amount": float('inf')}
    
    for row in csv_data:
        current_value = int(row[1])
        month = row[0]
        
        if row[0] != "":
            total_months += 1
            total_profit_loss += current_value
            
            
            if previous_value is not None:
                change = current_value - previous_value
                monthly_changes.append(change)
                if change > gi["amount"]:
                    gi["amount"] = change
                    gi["month"] = month
                
                
                if change < gd["amount"]:
                    gd["amount"] = change
                    gd["month"] = month
        previous_value = current_value     
        
    average_change = sum(monthly_changes) / len(monthly_changes) if monthly_changes else 0
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_loss}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {gi['month']} (${gi['amount']})\n"
        f"Greatest Decrease in Profits: {gd['month']} (${gd['amount']})\n"
    )
    
    print(output)
    output_file = os.path.join(output_dir, "financial_analysis.txt")
    with open(output_file, 'w') as txt_file:
        txt_file.write(output)
        
        
       


