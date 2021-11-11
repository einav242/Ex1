import csv

from Ex1.src.ListOfCallForElevator import ListOfCallForElevator


def write_from_csv(file1, file2):
    with open(file1, 'w', newline="") as f:
        writer = csv.writer(f)
        calls = ListOfCallForElevator(file2)
        writer.writerows(calls.Call)


if __name__ == '__main__':
    write_from_csv("bar", "Calls_a.csv")
