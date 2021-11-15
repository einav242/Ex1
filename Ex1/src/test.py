import csv

from Ex1.src.SmartElevatorAlgo import SmartElevatorAlgo
from Ex1.src.CallForElevator import CallForElevator
from Ex1.src.ListOfCallForElevator import ListOfCallForElevator


def elevator_assignment(file1, file2):
    calls = ListOfCallForElevator(file1)
    for k in range(len(calls.Call)):
        calls.Call[k].index = 0

    with open(file2, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(calls.Call)


if __name__ == '__main__':
    algo = SmartElevatorAlgo("B2.json", "Calls_a.csv", "output.csv")
    algo.elevator_assignment()

