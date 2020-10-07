import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1

        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley + 1

Khan_Percentage = (Khan/total_votes)*100
Correy_percentage = (Correy/total_votes)*100
Li_percentage = (Li/total_votes)*100
OTooley_percentage = (OTooley/total_votes)*100

if Khan > Correy and Li and OTooley:
    Winner = "Khan"
elif Correy > Khan and Li and OTooley:
    Winner = "Correy"
elif Li > Khan and Correy and OTooley:
    Winner = "Li"
elif OTooley > Khan and Correy and Li:
    Winner = "O'Tooley"

print("Election Results\n-------------------------")
print(f"Total Votes: {str(total_votes)}\n-------------------------")
print(f"Khan: {Khan_Percentage:.3f}% ({Khan})")
print(f"Corry: {Correy_percentage:.3f}% ({Correy})")
print(f"Li: {Li_percentage:.3f}% ({Li})")
print(f"O'Tooley: {OTooley_percentage:.3f}% ({OTooley})\n-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")