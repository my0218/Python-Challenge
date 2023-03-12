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

print ("Election Results")
print ("---------------------")
print (candidate_list)
print ("Total Votes: ", rowcount)
print ("---------------------")
print ("Charles Casper Stockham: ", candidate1_pct,"% (", candidate1_votes, ")")
print ("Diana DeGette: ", candidate2_pct, "% (", candidate2_votes, ")")
print ("Raymon Anthony Doane: ", candidate3_pct, "% (", candidate3_votes, ")")
print ("Winner: ", winner)