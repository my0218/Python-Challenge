import os
import csv

# Set up variables to store data

rowcount = 0
total_profit_losses = 0
previous_month_profit = 0
average_change = 0
greatest_increase_month = ""
greatest_increase = 0
greatest_decrease_month = ""
greatest_decrease = 0

# Open the CSV file and read in the data
with open('PyBank/Resources/budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    next(csvreader) 
    for row in csvreader:
        rowcount += 1
        month = row[0]
        profit_losses = int(row[1])
        
        # Calculate the total profit/losses
        total_profit_losses += profit_losses
        
        # Calculate the change in profit from the previous month
        change = profit_losses - previous_month_profit
        
        # Update the previous month's profit for the next iteration
        previous_month_profit = profit_losses
        
        # Calculate the average change
        if month != "Jan-10": # exclude first month from average calculation
            average_change += change
        
        # Find the greatest increase and decrease in profits
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = month
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = month

        # Calculate the average change (exclude first month)
        average_change /= rowcount
        

# Output the results
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {rowcount}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)
print (output)

with open ("PyBank/Analysis/final.txt", "w") as txtfile:
    txtfile.write (output)
txtfile.close()