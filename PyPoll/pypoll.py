import os
import csv

#list to store data
candidate_list = []
rowcount = 0
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate1_pct = 0
candidate2_pct = 0
candidate3_pct = 0

# Open the CSV file and read in the data
with open('PyPoll/Resources/election_data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip header row
    next(csvreader) 

    #count number of votes
    for row in csvreader:
        rowcount += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    #get votes of each candidates
        if str(row[2]) == "Charles Casper Stockham":
            candidate1_votes +=1
        elif str(row[2]) == "Diana DeGette":
            candidate2_votes +=1
        else:
            candidate3_votes +=1
    # vote percentage of each candidates
        candidate1_pct = round((candidate1_votes / rowcount) *100, 3)
        candidate2_pct = round((candidate2_votes / rowcount) *100, 3)
        candidate3_pct = round((candidate3_votes / rowcount) *100, 3)

    result = {"Charles Casper Stockham":candidate1_votes, "Diana DeGette": candidate2_votes, "Raymon Anthony Doane": candidate3_votes}
    winner = max (result, key=result.get)

output = (
    f"\nElection Results\n"
    f"---------------------\n"
    f"{candidate_list}\n"
    f"Total Votes: {rowcount}\n"
    f"---------------------\n"
    f"Charles Casper Stockham: {candidate1_pct} % ({candidate1_votes} )\n"
    f"Diana DeGette: {candidate2_pct} % ({candidate2_votes})\n"
    f"Raymon Anthony Doane: {candidate3_pct} % ({candidate3_votes})\n"
    f"Winner: {winner}\n"
)

print (output)

with open ("PyPoll/Analysis/final.txt", "w") as txtfile:
    txtfile.write (output)
txtfile.close()