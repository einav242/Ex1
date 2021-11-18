

import sys

from Ex1.src.SmartAlgo import SmartElevatorAlgo
from Ex1.data.Ex1_input.Ex1_Calls import *
from Ex1.data.Ex1_input.Ex1_Buildings import *

if __name__ == '__main__':

    if len(sys.argv) == 4:
        algo = SmartElevatorAlgo(sys.argv[1], sys.argv[2], sys.argv[3])
        algo.elevator_assignment()
    else:
        b = str(input("please insert the building name"))
        calls = str(input("please insert the calls file name"))
        output = str(input("please insert the output name"))
        if b != "" and calls != "" and output != "":
            algo = SmartElevatorAlgo(b, calls, output)
            algo.elevator_assignment()
        else:
            algo = SmartElevatorAlgo("B1.json", "Calls_a.csv", "output1.csv")
            algo.elevator_assignment()
