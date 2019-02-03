import csv
import os
filepath = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))),"Resources","budget_data.csv")
with open("Resources/budget_data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    numberOfMonths = 0
    netAmount = 0
    greatestIncrease = 0
    greatestDecrease = 0
    next(csvreader, None) # skips the headers

    for row in csvreader:
        numberOfMonths += 1
        netAmount += int(row[1])
        if int(row[1]) > greatestIncrease:
            greatestIncrease = int(row[1])
            greatestIncreaseMonth = row[0]
        if int(row[1]) < greatestDecrease:
            greatestDecrease = int(row[1])
            greatestDecreaseMonth = row[0]

    averagechange = netAmount / numberOfMonths
    averagechange = averagechange * 100 // 1 / 100

print("Financial analysis")
print("------------------")
print("Total Months: ", numberOfMonths)
print("Total: $", netAmount)
print("Average Change: ", averagechange)
print("Greatest Increase in Profits: ", greatestIncreaseMonth, " ($", greatestIncrease, ")")
print("Greatest Decrease in Profits: ", greatestDecreaseMonth, " ($", greatestDecrease, ")")