# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:05:34 2020

@author: bader
"""

import os
import csv


budget_csv = os.path.join("Resources", "budget_data.csv")
#os.path.join("Users", "bader", "Desktop", "BootCamp_HW_Assignments", "HW3(Python)", "Python-Challenge", "PyBank", "Resources", "budget_data.csv")
   # '/Users/bader/Desktop/BootCamp_HW_Assignments/HW3(Python)/Python-Challenge/PyBank/Resources/budget_data.csv'
number_months = 0
total_profit_loss = []
average = []
month = []

#average_profit_loss = 0
with open(budget_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
 

    for row in csvreader:
        number_months += 1 
        profit_loss = int(row[1])
        if number_months == 1:
            difference = 0
           # average.append(difference)
        else:
            difference =  - (total_profit_loss[-1] -profit_loss)
            average.append(difference)
        total_profit_loss.append(profit_loss)
        month.append(row[0])

max_increase_month = average.index(max(average)) + 1
max_decrease_month = average.index(min(average)) + 1

print("Financial Analysis\n---------------------------" )

print(f"\nTotal months: "+ str(number_months))
print(f"Profit/ Loss: {sum(total_profit_loss)}")
print(f"average: {round(sum(average)/len(average))}")
print(f"Greatest increase in profits: " + str(month[max_increase_month]) +" "+ str(max(average)))
print(f"Greatest decrease in profits: " + str(month[max_decrease_month]) +" "+ str(min(average)))


Text_file = os.path.join("Analysis", "budget_data_output.txt")

with open(Text_file, "w") as file:
    file.write("Financial Analysis\n---------------------------" )
    file.write("\nTotal months: "+ str(number_months))
    file.write("\nProfit/ Loss: {sum(total_profit_loss)}")
    file.write("\naverage: {round(sum(average)/len(average))}")
    file.write("\nGreatest increase in profits: " + str(month[max_increase_month]) +" "+ str(max(average)))
    file.write("\nGreatest decrease in profits: " + str(month[max_decrease_month]) +" "+ str(min(average)))

