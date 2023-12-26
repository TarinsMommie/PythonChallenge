import os

import csv

# Define the file path
file_path = "budget_data.csv"

# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract the date and profit/loss from the row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        # Calculate the change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            # Update greatest increase and decrease
            if change > greatest_increase[1]:
                greatest_increase = [date, change]
            elif change < greatest_decrease[1]:
                greatest_decrease = [date, change]

        # Update previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / (total_months - 1)

# Print the results
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Save the results to a text file
output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(f"Results saved to {output_file_path}")