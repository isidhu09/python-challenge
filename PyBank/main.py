#importing modules
import os
import csv

#Set path for file
csvpath = os.path.join('','Resources','budget_data.csv')

#Open the CSV file
with open(csvpath, encoding='utf') as csvfile:

#   CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

#   Read the header row first 
    csv_header = next(csvreader)

#   Creating lists and setting variables
    date = []
    monthlyChangePL = []
    totalMonth = 0
    totalDollar = 0
    totalChange = 0
    beginAmount = 0

#----------------------BEGIN Loop----------------------
    for row in csvreader:

#       Adding dates into list to use later for identifying date for greatest increase and decrease
        date.append(row[0])
        
#       Calculations for total month count and total dollar value
        totalMonth +=1
        totalDollar += int(row[1])

#       Setting the end amount to subtract beginning from to month over month change
        endAmount = int(row[1])

#       Calculating monthly change and adding it to the monthly change list
        monthlyChange = endAmount - beginAmount
        monthlyChangePL.append(monthlyChange)

#       Setting the begging amount equal to the end index to then move down the months for the monthly change
        beginAmount = endAmount

#       Finding the max and min values in the monthly change list
        greatestIncrease = max(monthlyChangePL)
        greatestDecrease = min(monthlyChangePL)

#       Locating the date from the index value of the monthly change list
        iDate = date[monthlyChangePL.index(greatestIncrease)]
        dDate = date[monthlyChangePL.index(greatestDecrease)]
#----------------------END Loop------------------------    

#   To calculate average we will need the sum of the values in the monthly change list with the very first value subtracted out
    totalChange = sum(monthlyChangePL)-monthlyChangePL[0]

#   Calculating average change in profit with 1 less the monthly count since we removed the first value which was used initally to find the monthly change
    avgChange = (totalChange/(int(totalMonth)-1))
    
#   Setting output into list to later write into text file
output=[("Financial Analysis"),
    ("----------------------------"),   
    (f"Total Months: {totalMonth}"),
    (f"Total: ${totalDollar}"), 
    (f"Average Change: ${round(avgChange,2)}"),
    (f"Greatest Increase in Profits: {iDate} (${greatestIncrease})"),
    (f"Greatest Decrease in Profits: {dDate} (${greatestDecrease})")]

#----------------------BEGIN Loop----------------------
#Loop to properly display output in terminal
for out in output:
    print(out)
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
#----------------------END Loop------------------------ 
