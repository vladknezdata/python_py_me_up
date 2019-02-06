import os
import csv
from us_state_abbrev import us_state_abbrev as abb

input_path = os.path.join(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "Resources", "employee_data.csv"))
output_path = os.path.join(
    os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", "Resources", "new_employee_data.csv"))

def nameConversion(name):
    return name.split(" ")

def dateOfBirthConvrsion(dob):
    dobSplit = dob.split("-")
    newDob = str.join("/", (dobSplit[1], dobSplit[2],dobSplit[0]))
    return newDob

def ssnConversion(ssn):
    return "***-**-" + ssn[7:]

with open(input_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    headers = next(csvreader)
    headers.insert(2, "Last Name")

    newData = []
    for row in csvreader:
        newData.append([row[0], nameConversion(row[1])[0], nameConversion(row[1])[1],
        dateOfBirthConvrsion(row[2]), ssnConversion(row[3]), abb[row[4]]])

with open(output_path, 'w', newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    for i in range(len(newData)):
        csvwriter.writerow(newData[i])