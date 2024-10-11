# Import necessary libraries
import os
import csv

# File path to the dataset
file_to_load = os.path.join('Resources','budget_data.csv')  # Input file path

# Initialize variables
total_months = 0
total_profit = 0
changes = []
previous_profit = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the csv file
with open(file_to_load, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    header = next(csvreader)
    
    # Read the first row (to initialize previous_profit)
    first_row = next(csvreader)
    total_months += 1
    total_profit += int(first_row[1])
    previous_profit = int(first_row[1])
    
    # Loop through the rest of the data
    for row in csvreader:
        # Update total months
        total_months += 1
        
        # Update total profit
        total_profit += int(row[1])
        
        # Calculate the change in profit/loss
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        
        # Find greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        
        # Find greatest decrease in profits
        if change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the results to a text file
file_to_output = os.path.join("analysis", "budget_analysis.txt")
with open(file_to_output, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")