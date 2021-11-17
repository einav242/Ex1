import sys

from Ex1.src.SmartAlgo import SmartElevatorAlgo


if __name__ == '__main__':
    algo = SmartElevatorAlgo(sys.argv[1], sys.argv[2], sys.argv[3])
    algo.elevator_assignment()
