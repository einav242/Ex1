
import csv

from Ex1.src.Building import Building

from Ex1.src.ListOfCallForElevator import ListOfCallForElevator


class SmartElevatorAlgo:

    def __init__(self, building, calls, output):
        self._building = Building(building)
        self.list_of_call = ListOfCallForElevator(calls)
        self.output = output

    def __iter__(self):
        return iter([self._building, self._list_of_call, self.output])

    def elevator_assignment(self):
        for k in self.list_of_call:
            self.list_of_call.Call[k].index = 0

        with open(self.output, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.list_of_call.Call)




