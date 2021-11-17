import csv
import sys

from Ex1.src.Building import Building
from Ex1.src.ListOfCallForElevator import ListOfCallForElevator


class SmartElevatorAlgo:

    def __init__(self, building, calls):
        self.building = Building(building)
        self.list_of_call = ListOfCallForElevator(calls).Call

    def __iter__(self):
        return iter([self.building, self.list_of_call])

    def elevator_assignment(self):
        ID = 0
        if self.building.number_of_elevator == 1:
            for k in range(len(self.list_of_call)):
                self.list_of_call[k].index = 0
                self.list_of_call[k].id = 0

        else:
            for j in range(len(self.list_of_call)):
                curr = self.list_of_call[j]
                if curr.id == -1:
                    curr.id = ID
                    ID += 1
                    i = j
                    for k in range(j + 1, len(self.list_of_call)):  # **
                        curr_temp = self.list_of_call[i]
                        next_curr = self.list_of_call[k]
                        if next_curr.id == -1 and curr_temp.direction() == next_curr.direction() \
                                and curr_temp.dest == next_curr.dest:
                            if self.check_path(curr_temp, next_curr, k):
                                if next_curr.index == -1 and curr_temp.index == -1:
                                    e = -1
                                    min_call = sys.maxsize
                                    for m in range(len(self.building.elevators)):
                                        T = self.building.elevators[m].time_of_path(curr_temp.src, next_curr.src)
                                        T += curr_temp.time
                                        t = next_curr.time
                                        if T >= t:
                                            if len(self.building.elevators[m].list_elev) < min_call:
                                                e = m
                                                min_call = len(self.building.elevators[m].list_elev)
                                    if e != -1:
                                        curr_temp.index = e
                                        next_curr.index = e
                                        next_curr.id = curr_temp.id
                                        curr_temp.dest = next_curr.src
                                        i = k
                                        self.building.elevators[e].list_elev.append(curr_temp)
                                        self.building.elevators[e].list_elev.append(next_curr)
                                elif curr_temp.index != -1 and next_curr.index == -1:
                                    e = curr_temp.index
                                    T = self.building.elevators[e].time_of_path(curr_temp.src, next_curr.src)
                                    T += curr_temp.time
                                    t = next_curr.time
                                    if T >= t:
                                        next_curr.index = e
                                        next_curr.id = curr_temp.id
                                        curr_temp.dest = next_curr.src
                                        i = k
                                        ind = self.building.elevators[e].list_elev.index(curr_temp)
                                        self.building.elevators[e].list_elev.insert(ind + 1, next_curr)
                                elif next_curr != -1 and curr_temp != -1:
                                    i = k

        for k in range(len(self.list_of_call)):
            e = -1
            min_call = sys.maxsize
            if self.list_of_call[k].index == -1:
                for i in range(len(self.building.elevators)):
                    if len(self.building.elevators[i].list_elev) < min_call:
                        min_call = len(self.building.elevators[i].list_elev)
                        e = i
                self.list_of_call[k].index = e
                self.building.elevators[e].list_elev.append(self.list_of_call[k])

    def check_path(self, call1, call2, k) -> bool:
        if call1.direction == 1:  # up
            if call1.src <= call2.src:
                return True
            if call1.index != -1:
                m = k
                while m > 0:
                    if call1.id == self.list_of_call[m - 1].id:
                        if self.list_of_call[m - 1].src <= call2.src:
                            if self.check_time(self.list_of_call[m - 1], call2, call1.index):
                                return True
                    m -= 1
            return False
        else:  # down
            if call1.src >= call2.src:
                return True
            if call1.index != -1:
                m = k
                while m > 0:
                    if call1.id == self.list_of_call[m - 1].id:
                        if self.list_of_call[m - 1].src >= call2.src:
                            if self.check_time(self.list_of_call[m - 1], call2, call1.index):
                                return True
                    m -= 1
            return False

    def check_time(self, call1, call2, e) -> bool:
        T = self.building.elevators[e].time_of_path(call1.src, call2.src)
        T += call1.time
        t = call2.time
        if T >= t:
            ind = self.building.elevators[e].list_elev.index(call1)
            call2.index = e
            call2.id = call1.id
            temp = call1.dest
            call1.dest = call2.src
            call2.dest = temp
            self.building.elevators[e].list_elev.insert(ind + 1, call2)
            return True
