import csv
import os

input_path = os.path.join(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),"..", "Resources", 'election_data.csv'))
output_path = os.path.join(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),"..", "Resources", 'ElectionResults.txt'))
with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    totalNumberOfVotes = 0
    candidates = []
    votes = []

    next(csvreader, None) # skip the headers

    for row in csvreader:
        totalNumberOfVotes += 1
        if row[2] in candidates:
           votes[candidates.index(row[2])] += 1
        else:
            candidates.append(row[2])
            votes.append(1) 

#   creating a txt file

with open(output_path, 'w', newline="") as textfile:

    textfile.write("\n")
    textfile.write("Election results\n")
    textfile.write("-------------------------\n")
    textfile.write("Total Votes: " + str(totalNumberOfVotes) + "\n")
    textfile.write("-------------------------\n")

    for i in range(len(candidates)):
        textfile.write(candidates[i] + ": " + str(format(votes[i]/totalNumberOfVotes*100, '.3f')) + "% (" + str(votes[i]) + ")\n")

    textfile.write("-------------------------\n")
    textfile.write("Winner: " + candidates[votes.index(max(votes))] + "\n")
    textfile.write("-------------------------\n")

#   opening created txt and printing it
with open(output_path, newline="") as f:
    for line in f:
        print(line, end="")