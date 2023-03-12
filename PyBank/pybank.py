import os
import csv

# Set up variables to store data

total_month = 0
total_profit_losses = 0
previous_month_profit = 0
change = average_change = 0
change_list = []
greatest_increase_month = ""
greatest_increase = 0
greatest_decrease_month = ""
greatest_decrease = 0

# Open the CSV file and read in the data
with open('Resources/budget_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    next(csvreader) 
    for row in csvreader:
        total_month = total_month + 1
        month = row[0]
        profit_losses = int(row[1])
        
        # Calculate the total profit/losses
        total_profit_losses += profit_losses
        
        # Calculate the change in profit from the previous month
        change = profit_losses - previous_month_profit
        
        # Update the previous month's profit for the next iteration
        previous_month_profit = profit_losses
        
        # Calculate the average change
        if month!= "Jan-10":
            average_change = 0
        
            change_list = change_list + [change]
            average_change = sum (change_list) / len(change_list)

        # Find the greatest increase and decrease in profits
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = month
        elif change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = month  

# Output the results
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)
print (output)

with open ("Analysis/final.txt", "w") as txtfile:
    txtfile.write (output)
txtfile.close()