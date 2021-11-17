import csv
import sys

from Ex1.src.SmartAlgo import SmartElevatorAlgo

if __name__ == '__main__':
    algo = SmartElevatorAlgo(sys.argv[1], sys.argv[2])
    algo.elevator_assignment()
    with open(sys.argv[3], 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerows(algo.list_of_call)
