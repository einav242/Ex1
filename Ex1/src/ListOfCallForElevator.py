import csv

from Ex1.src.CallForElevator import CallForElevator


class ListOfCallForElevator:
    def __init__(self, file_csv):
        with open(file_csv) as f:
            reader = csv.reader(f)
            self.Call = []
            for rows in reader:
                self.Call.append(CallForElevator(rows))

    def __iter__(self):
        for k in range(len(self.Call)):
            return iter(self.Call(k))

    def __str__(self):
        st = ""
        for k in range(len(self.Call)):
            st += str(self.Call[k])
        return st
