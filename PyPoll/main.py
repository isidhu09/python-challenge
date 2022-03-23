#importing modules
import os
import csv

#Set path for file
csvpath = os.path.join('','Resources','election_data.csv')

#Open the CSV file
with open(csvpath, encoding='utf') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    x = 0
    for row in csvreader:
        print(row)
        x +=1
    print(x)  