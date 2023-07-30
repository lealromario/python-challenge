#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import dependencies
import csv
import os


# In[3]:


# Creating the path
find_path = "C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyPoll/Resources/election_data.csv"

total_votes = 0
candidates_votes = {}
winner_count = 0
percent_candidates_votes = {}


# In[6]:


# Opening and reading csv file
with open(find_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

# Loop through looking for canditates
    for row in csv_reader:

        # The total number of votes cast
        total_votes = total_votes + 1

        # A complete list of candidates who received votes and The total number of votes each candidate won
        if row[2] in candidates_votes:
            candidates_votes[row[2]] += 1
        else:
            candidates_votes[row[2]] = 1

        # The percentage of votes each candidate won
        for key, velue in candidates_votes.items():
            percent_candidates_votes[key] =round((velue/total_votes)* 100 , 3)

        # The winner of the election based on popular vote.
            if percent_candidates_votes[key] > winner_count:
                winner_count = candidates_votes[key]
                winner = key


# In[9]:


# Displaying information
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for key, velue in candidates_votes.items():
    print(key,':' , str(percent_candidates_votes[key]),'%','  ','(',candidates_votes[key],')')
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")


# In[18]:


# create the analysis file
f = open("C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyPoll/Resources/election_analysis.txt", "w")

with open("C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyPoll/Resources/election_analysis.txt", "w") as f:
    f.write(f"Election Results\n")
    f.write(f"-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for key, velue in candidates_votes.items():
        f.write(f"{key}: {str(percent_candidates_votes[key])}%   ({candidates_votes[key]})\n")
    f.write(f"-------------------------\n")
    f.write(f"Winner: {winner}\n")
    f.write(f"-------------------------\n")
             
    
# Close the new file
f.close()

