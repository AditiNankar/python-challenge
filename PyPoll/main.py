# Import necessary libraries
import os
import csv

# File path to the dataset
file_to_load = os.path.join('Resources', 'election_data.csv')  # Input file path

# Initialize variables
total_votes = 0
candidates = {}

# Open and read the csv file
with open(file_to_load, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    header = next(csvreader)
    
    # Loop through each row in the dataset
    for row in csvreader:
        # Count the total number of votes
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # Track the candidate's vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the results
winner = ""
max_votes = 0
output = []

# Prepare the election results
output.append("Election Results")
output.append("-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append("-------------------------")

for candidate, votes in candidates.items():
    # Calculate the percentage of votes
    percentage = (votes / total_votes) * 100
    output.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Determine the winner
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output.append("-------------------------")
output.append(f"Winner: {winner}")
output.append("-------------------------")

# Print the analysis to the terminal
for line in output:
    print(line)

# Export the results to a text file
output_path = os.path.join("analysis", "election_results.txt")
with open(output_path, "w") as txtfile:
    for line in output:
        txtfile.write(line + "\n")