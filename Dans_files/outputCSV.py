import csv

# This will overwrite the file to setup just the headers
def setupCSVHeaders():
    with open("output.csv", "w") as csv_file:
        csv_wr = csv.writer(csv_file)
        csv_wr.writerow(["Test Case", "Passed", "Expected Result", "Actual Result"])
        csv_file.close()

# This appends new line each time it is called
def outputCSV(testCase, outcome, expectedResult, actualResult):
    with open("output.csv", "a", newline="") as csv_file:
        csv_app = csv.writer(csv_file)
        csv_app.writerow([testCase, outcome, expectedResult, actualResult])
        csv_file.close()





