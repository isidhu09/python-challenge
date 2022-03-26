#importing modules
import os
import csv

#Set path for file
csvpath = os.path.join('','Resources','election_data.csv')

#Open the CSV file
with open(csvpath, encoding='utf') as csvfile:

#   CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

#   Read the header row first 
    csv_header = next(csvreader)

#   Creating lists and setting variables
    totalVotes = 0
    candidates = []
    cVotes = []

#----------------------BEGIN Loop----------------------
    for row in csvreader:
        
#       Calculations for total vote count
        totalVotes +=1

#       Setting candidate for each row to put into the candidates list
        candidate = row[2]

#       If statement to calculate votes, by checking if the candidate is in the list and adding 1 to each vote count
        if candidate in candidates:
            cVotes[candidates.index(candidate)] +=1
#       If the candidate is not there then it makes a spot for the candidate
        else:
            candidates.append(candidate)
            cVotes.append(1)
#----------------------END Loop------------------------ 

#Getting index of the highest vote in the cVote list
index_max = max(range(len(cVotes)), key=cVotes.__getitem__)

#   Setting outputs into list to later write into text file
output=[("Election Results"),
    ("----------------------------"),  
    (f"Total Votes: {totalVotes}"),
    ("----------------------------")]
output2=[("----------------------------"),  
    (f"Winner: {candidates[index_max]} "),
    ("----------------------------")]

#----------------------BEGIN Loop----------------------
#Loop to properly display output in terminal
for out in output:
    print(out)
#----------------------END Loop------------------------ 

#----------------------BEGIN Loop----------------------
#Loop to print each candidate with their percent of votes (rounded to 3 decimal places) and total votes
for candidate in candidates:
    print(f"{candidate}: {round(cVotes[candidates.index(candidate)]/totalVotes *100,3)}% ({cVotes[candidates.index(candidate)]})")
#----------------------END Loop------------------------ 

#----------------------BEGIN Loop----------------------
#Loop to properly display output in terminal
for out2 in output2:
    print(out2)
#----------------------END Loop------------------------

#Set path for file
txtpath = os.path.join('','Analysis','results.txt')

#Writing to the txt file
with open(txtpath, 'w') as textfile:

#----------------------BEGIN Loop----------------------
#   Loop to run through each value in the list and add it to a seperate line in the text file using '\n'
    for out in output:
        textfile.write(out)
        textfile.write('\n')
    for candidate in candidates:
        textfile.write(f"{candidate}: {round(cVotes[candidates.index(candidate)]/totalVotes *100,3)}% ({cVotes[candidates.index(candidate)]})")
        textfile.write('\n')
    for out2 in output2:
        textfile.write(out2)
        textfile.write('\n')
#----------------------END Loop------------------------ 