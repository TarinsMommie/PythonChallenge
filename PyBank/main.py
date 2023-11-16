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
#Number of Months:
column_index = 0
    if not header_skipped:
        header_skipped = True
        continue 
    Total_Months += 1
    print (f'Total Months: {Total_Months}")
#Average Change:
column_index = 1
    if not header_skipped:
        header_skipped = True
        continue 
    Average_Net_Loses += 1
    print (f'Average Change: {Average_Net_Loses")
    