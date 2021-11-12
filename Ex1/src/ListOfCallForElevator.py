import csv

from Ex1.src.CallForElevator import CallForElevator


class ListOfCallForElevator:
    def __init__(self, file_csv):
        with open(file_csv) as f:
            reader = csv.reader(f)  # read from file_csv
            self.Call = []  # a list of Calls
            for rows in reader:  # rows of the file
                self.Call.append(CallForElevator(rows))  # append all the rows of Call For Elevator

    def __iter__(self):
        for k in range(len(self.Call)):
            return iter(self.Call(k))