import os
import csv

from numpy import average, greater
from prometheus_client import generate_latest

budgetpath = os.path.join("PyBank","Resources","budget_data.csv")

with open(budgetpath, 'r') as budget_data:
    budgetobject = csv.reader(budget_data,delimiter=",")
    next(budgetobject, None) #to remove first row

    no_month = 0  #define variable for *The total number of months included in the dataset
    netprofit_loss = 0 #define variable for *The net total amount of "Profit/Losses" over the entire period

    change=0
    change_in_PL = [] #define array for *The changes in "Profit/Losses" over the entire period, and then the average of those changes
    dateforprofitchange=[] #define list for items in first column, counting from 2nd date

    profitprevious=0

    for row in budgetobject:
        no_month += 1
        netprofit_loss += int(row[1])

#change  of profit
        if no_month>=2:
            change=(int(row[1])-profitprevious)
            change_in_PL.append(change) #add to the list of changes in profit/loss

            dateinrow=row[0]
            dateforprofitchange.append(dateinrow) #start dates to correspond to change_in_PL
        profitprevious = int(row[1])

    totalchange=sum(change_in_PL)
    averagechange = totalchange/len(change_in_PL)

    greatestincrease = 0
    greatestdecrease = 0
    i = 0  #var to keep track of index for greatest increase
    d = 0  #var to keep track of index for greatest decrease

    rownumber=0
    for singlechange in change_in_PL:
            rownumber +=1
            if greatestincrease< singlechange:
                greatestincrease = singlechange
                i = rownumber -1
            if greatestdecrease > singlechange:
                greatestdecrease = singlechange
                d = rownumber -1


# print(f"ElectionResults\nBlahBlah\")  
# the \n to introduce new line in Python
# \at the end of row indicates code continues next line

finaltext=(f"Financial Analysis\n----------------------------\nTotal Months: {no_month}\nTotal: ${netprofit_loss}\
    \nAverage Change: ${round(averagechange,2)}\nGreatest Increase in Profits: {dateforprofitchange[i]} (${greatestincrease})\
    \nGreatest Decrease in Profits: {dateforprofitchange[d]} (${greatestdecrease})")

# print the analysis to the terminal 
print(finaltext)    

# export a text file with the results.
budgetanalysispath = os.path.join("PyBank","analysis","budget_output.txt")
with open(budgetanalysispath,'w') as budgetout:
    budgetout.write(finaltext)

### Assignment completed on 09/10/2022 MD ###





