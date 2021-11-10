import csv

from Ex1.src.CallForElevator import CallForElevator


class ListOfCallForElevator:
    def __init__(self, file_csv):

        with open(file_csv) as f:
            reader = csv.reader(f)
            self_Call = []
            for rows in reader:
                self_Call.append(CallForElevator(rows))
