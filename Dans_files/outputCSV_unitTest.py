import unittest
import csv

class MyTestCase(unittest.TestCase):
    def test_outputCSV(self):
        testCase = "This is a test"
        outcome = "False"
        expectedResult = 1004
        actualResult = 1005

        with open("output_unitTest.csv", "w", newline="") as csv_file:
            csv_wr = csv.writer(csv_file)
            csv_wr.writerow(["Test Case", "Failed", "Expected Result", "Actual Result"])
            csv_wr.writerow([testCase, outcome, expectedResult, actualResult])
            csv_file.close()

        with open("output_unitTest.csv", "r") as csv_file_test:
            csv_reader = csv.reader(csv_file_test)
            line_count = 0
            for row in csv_reader:
                testCaseRead = row[0]
                outcomeRead = row[1]
                expectedResultRead = row[2]
                actualResultRead = row[3]
            csv_file_test.close()

        # Testing that all values outputted to csv are done in a correct manner
        self.assertEqual(testCase, testCaseRead)
        self.assertEqual(outcome, outcomeRead)
        self.assertEqual(expectedResult, int(expectedResultRead))
        self.assertEqual(actualResult, int(actualResultRead))


if __name__ == '__main__':
    unittest.main()
