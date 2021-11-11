import csv

from Ex1.src.CallForElevator import CallForElevator


class ListOfCallForElevator:
    def __init__(self, file_csv):
        with open(file_csv) as f:
            reader = csv.reader(f)
            self.Call = []
            my_list = []
            for rows in reader:
                my_list.append(str(rows[0]))
                my_list.append(float(rows[1]))
                my_list.append(int(rows[2]))
                my_list.append(int(rows[3]))
                my_list.append(int(rows[4]))
                my_list.append(int(rows[5]))
                self.Call.append(my_list)

    def __iter__(self):
        for k in range(len(self.Call)):
            for m in range(0, 6):
                return iter([self.Call[k][m]])
