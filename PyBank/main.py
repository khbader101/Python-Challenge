# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 17:05:34 2020

@author: bader
"""

import os
import csv

budget_csv = "/Users/bader/Desktop/BootCamp_HW_Assignments/HW3(Python)/Python-Challenge/PyBank/Resources/budget_data.csv"
#os.path.join('..', 'Desktop', 'BootCamp_HW_Assignments', 'HW3(Python)', 'Python-Challenge', 'PyBank', 'Resources', 'budget_data.csv')


with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)
    print(csvreader)
    
    for row in csvreader:
        print(row)
