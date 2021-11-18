import json

from Elevators import Elevators


class Building:

    def __init__(self, file_name):
        with open(file_name, "r") as fp:

            di = json.load(fp)  # load the json building
            self._minFloor = di["_minFloor"]  # min_floor
            self._maxFloor = di["_maxFloor"]  # max_floor
            self.elevators = []  # list of elevators
            for k in di["_elevators"]:
                self.elevators.append(Elevators(k))  # append to the list of elevator
            self.number_of_elevator = len(self.elevators)
