from enum import unique
import os
import csv

inputpath = os.path.join("PyPoll","Resources","election_data.csv")
with open(inputpath,'r') as electionfile:
    electiondata=csv.reader(electionfile,delimiter=",")
    next(electiondata, None)

    totalvote = 0
    candidatelist = []
    uniquelist = []  #var to provide list of candidates

    for row in electiondata:
        totalvote += 1
        candidate=row[2]
        candidatelist.append(candidate)
        if candidate not in uniquelist:
            uniquelist.append(candidate)
    #    print(totalvote) #checked to be correct 09/10/2022
    #    print(uniquelist) #checked ok 09/10/2022
     
#create array [0, 0, ...,0] to count votes for each candidate
    count_individual_vote = [] 
    for a in range(len(uniquelist)):
        count_individual_vote.append(0)
    print (count_individual_vote)


    # for personelected in uniquelist:
    #         print(personelected)
    #         print(uniquelist.index(personelected))

#start counting vote and adding to the corresponding index for the array above
    for row in electiondata:
        for personelected in uniquelist:
            print(personelected)
            print(uniquelist.index(personelected))
            if row[2] == personelected:
                count_individual_vote[uniquelist.index(personelected)] +=1
    print(count_individual_vote)    
  

# finaltext = (f"Election Results\n-------------------------\
#     \nTotal Votes: {totalvote}369711
#   -------------------------
#   Charles Casper Stockham: 23.049% (85213)
#   Diana DeGette: 73.812% (272892)
#   Raymon Anthony Doane: 3.139% (11606)
#   -------------------------
#   Winner: Diana DeGette
#   -------------------------
#   ```")