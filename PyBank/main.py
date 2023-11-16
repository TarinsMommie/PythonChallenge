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
