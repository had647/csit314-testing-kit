import csv

def outputCSV(testCase, outcome, expectedResult, actualResult):
    with open("output.csv", "w") as csv_file:
        csv_app = csv.writer(csv_file)
        csv_app.writerow(["Test Case", "Failed", "Expected Result", "Actual Result"])
        csv_app.writerow([testCase, outcome, expectedResult, actualResult])






