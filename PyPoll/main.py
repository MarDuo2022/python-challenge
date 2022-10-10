import os
import csv

inputpath = os.path.join("./PyPoll","Resources","election_data.csv")
with open(inputpath,'r') as electionfile:
    electiondata=csv.reader(electionfile,delimiter=",")
    # next(electiondata, None) #skip header
    header=next(electiondata) #store header

    totalvote = 0
    candidatelist = []
    uniquelist = []  #var to provide list of candidates

    for row in electiondata:
        totalvote += 1
        candidate=row[2]
        candidatelist.append(candidate)
        if candidate not in uniquelist:
            uniquelist.append(candidate)
    # print(totalvote) #checked to be correct 09/10/2022
    # print(uniquelist) #checked ok 09/10/2022
     
#create array [0, 0, ...,0] to count votes for each candidate
    count_individual_vote = []
    for a in range(len(uniquelist)):
        count_individual_vote.append(0)
    # print (count_individual_vote)

#use candidatelist to count vote and adding to the corresponding index for the array above
    for candidate in candidatelist:
        if candidate in uniquelist:
            count_individual_vote[uniquelist.index(candidate)] +=1
    # print(count_individual_vote)
    
    percentage_vote = [] 
    for percent in count_individual_vote:
        percentage_vote.append(round(percent/totalvote*100,3))
    # print(percentage_vote)


    finaltextstart = (f"Election Results\n-------------------------\
    \nTotal Votes: {totalvote}\n-------------------------")
#print start text
    print(finaltextstart)

#print middle text
    winnerpercent=0.000
    for n in range(len(uniquelist)):
        if winnerpercent < percentage_vote[n]:
            winnerpercent = percentage_vote[n]
        print(f"{uniquelist[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

    finaltextend = (f"-------------------------\
    \nWinner: {uniquelist[percentage_vote.index(winnerpercent)]}\
    \n-------------------------")
#print final text
    print(finaltextend)

#write to the text file
middletext=[]
for n in range(len(uniquelist)):
    middletext.append(f"{uniquelist[n]}: {percentage_vote[n]}% ({count_individual_vote[n]})")

outputpath = os.path.join("PyPoll","analysis","election_output.txt")
with open(outputpath,'w') as electionout:

##USE PRINT
    electionout.write(finaltextstart)
    electionout.write("\n")
    electionout.write("\n".join(str(m) for m in middletext))
    electionout.write("\n")
    electionout.write(finaltextend)

###THE END###


#Appendix
#???????? WHY f-string does not work????
##TRY USING f-string 
#     electionout.write(print'{finaltextstart}\n\
# {"\n".join(str(m) for m in middletext)}\n\
# {finaltextend}')
#???????? WHY f-string does not work????


#further checkpoints:
    # for personelected in uniquelist:
    #         print(personelected)
    #         print(uniquelist.index(personelected))

#After reading once, 
#cannot reuse the same 'electiondata' as pointer is already to the bottom
    # for row in electiondata:
    #     DOES NOT WORK 2nd time within the 'with open....'