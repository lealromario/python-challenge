#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Import dependencies
import os
import csv


# In[6]:


# Create path to csv
find_path = "C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyBank/Resources/budget_data.csv"

output_file = "Financial Analysis.csv"
 
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []
    


# In[8]:


#Opening and reading the CSV file
with open(find_path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row (so that we track the changes properly)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after the header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])


# In[9]:


#Greatest increase in profits
greatest_increase = max(profits)
greatest_index = profits.index(greatest_increase)
greatest_date = dates[greatest_index]

#Greatest decrease (lowest increase) in profits 
greatest_decrease = min(profits)
worst_index = profits.index(greatest_decrease)
worst_date = dates[worst_index]

#Average change in "Profit/Losses between months over entire period"
avg_change = sum(profits)/len(profits)


# In[12]:


# Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})")


# In[15]:


# create the analysis file
f = open("C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyBank/Resources/profit_analysis.txt", "w")

with open("C:/Users/lealr/OneDrive/DU Bootcamp/Challenges/python-challenge/Starter_Code/PyBank/Resources/profit_analysis.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("---------------------\n")
    f.write(f"Total Months: {total_months}\n")
    f.write(f"Total: ${total_pl}\n")
    f.write(f"Average Change: ${round(avg_change, 2)}\n")
    f.write(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n")
    f.write(f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})\n")


# Closing the new file
f.close()


# In[ ]:




