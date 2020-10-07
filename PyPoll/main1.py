import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

total_votes = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0

with open(election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes.append(row)

        if row[2] == "Khan":
            Khan = Khan + 1
        elif row[2] == "Correy":
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] == "O'Tooley":
            OTooley = OTooley + 1

length_total_votes = len(total_votes)
Khan_Percentage = (Khan/length_total_votes)*100
Correy_percentage = (Correy/length_total_votes)*100
Li_percentage = (Li/length_total_votes)*100
OTooley_percentage = (OTooley/length_total_votes)*100

winner_Votes = max([Khan, Correy, Li, OTooley])
index = total_votes.index(winner_Votes)


print("Election Results\n-------------------------")
print(f"Total Votes: {str(length_total_votes)}\n-------------------------")
print(f"Khan: {Khan_Percentage:.3f}% ({Khan})")
print(f"Corry: {Correy_percentage:.3f}% ({Correy})")
print(f"Li: {Li_percentage:.3f}% ({Li})")
print(f"O'Tooley: {OTooley_percentage:.3f}% ({OTooley})\n-------------------------")

print(index)