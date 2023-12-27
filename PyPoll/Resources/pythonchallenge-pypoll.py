import os

import csv

# Define file path
file_path = "election_data.csv"

# Read CSV
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Define variables
    total_votes = 0
    candidates = {}
    winner = {"name": "", "votes": 0}

# Skip the header row
    header = next(csvreader)

    # Loop through the rows in the dataset
    for row in csvreader:
        # Extract candidate from the row
        candidate = row[2]

        # Count total number of votes
        total_votes += 1

        # Update candidates dictionary
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Update winner
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Save results to text file
output_file_path = "election_results.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Print results for each candidate
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")

print(f"Results saved to {output_file_path}")