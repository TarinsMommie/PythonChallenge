# Import os module
import os
# Module to read csv
import csv
#set path for file
budget_data = os.path.join("..","pybank","resources","budget_data.csv")
#open csv
with open(budget_data) as csvfile:
#csvreader
csv_reader = csv.reader(csv_file, delimiter=",")
#Count rows but not header
for row in csv_reader:
    if not header_skipped:
        header_skipped = True
        continue 
    Total_Months += 1
    print (f'Total Months: {Total_Months}")