import csv
import os

filepath = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))),"..","Resources","budget_data.csv")
output_path = os.path.join(os.path.join(
    os.path.dirname(os.path.abspath(__file__)),"..", "Resources", 'FinancialAnalysis.txt'))
with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    numberOfMonths = 0
    netAmount = 0
    greatestIncrease = 0
    greatestDecrease = 0
    change = 0
    
    next(csvreader, None) # skips the headers

    for row in csvreader:
        numberOfMonths += 1
        netAmount += int(row[1])
  
        if numberOfMonths > 1:
            change += int(row[1]) - previousMonth
        if int(row[1]) > greatestIncrease: # getting the min/max values
            greatestIncrease = int(row[1])
            greatestIncreaseMonth = row[0]
        if int(row[1]) < greatestDecrease:
            greatestDecrease = int(row[1])
            greatestDecreaseMonth = row[0]
        previousMonth = int(row[1])

    averagechange = change / (numberOfMonths - 1)


#   creating a txt file

with open(output_path, 'w', newline="") as textfile:

    textfile.write("Financial analysis\n")
    textfile.write("------------------\n")
    textfile.write("Total Months: " + str(numberOfMonths) + "\n")
    textfile.write("Total: $" + str(netAmount) + "\n")
    textfile.write("Average Change: " + format(averagechange, ".2f") + "\n")
    textfile.write("Greatest Increase in Profits: " + str(greatestIncreaseMonth) + " ($" + str(greatestIncrease) + ")\n")
    textfile.write("Greatest Decrease in Profits: " + str(greatestDecreaseMonth) + " ($" + str(greatestDecrease) + ")\n")

#   opening created txt and printing it

with open(output_path, newline="") as f:
    for line in f:
        print(line, end="")