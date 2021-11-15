import csv
import sys

from Ex1.src import CallForElevator
from Ex1.src.Building import Building

from Ex1.src.ListOfCallForElevator import ListOfCallForElevator


class SmartElevatorAlgo:

    def __init__(self, building, calls, output):
        self.building = Building(building)
        self.list_of_call = ListOfCallForElevator(calls).Call
        self.output = output

    def __iter__(self):
        return iter([self.building, self.list_of_call, self.output])

    def elevator_assignment(self):
        new_list = []
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
                    for k in range(j + 1, len(self.list_of_call.Call)):  # **
                        curr_temp = self.list_of_call[i]
                        next_curr = self.list_of_call[k]
                        if next_curr.id == -1:
                            if curr_temp.direction() == next_curr.direction():
                                if curr_temp.dest == next_curr.dest:
                                    if curr_temp.direction() == 1:  # up
                                        if self.check_path(curr_temp, next_curr, k):
                                            if curr_temp.index == -1:
                                                for m in range(len(self.building.elevators)):
                                                    T = self.building.elevators[m].time_of_path(curr_temp.src,
                                                                                                next_curr.src)
                                                    T += curr_temp.time
                                                    t = next_curr.time
                                                    if T >= t:
                                                        curr_temp.index = m
                                                        next_curr.index = m
                                                        next_curr.id = curr.id
                                                        curr_temp.dest = next_curr.src
                                                        i = k
                                                        new_list.append(curr_temp, next_curr)
                                            else:
                                                T = self.building.elevators[curr_temp.index].time_of_path(curr_temp.src,
                                                                                                          next_curr.src)
                                                T += curr_temp.time

                                                t = next_curr.time
                                                if T >= t:
                                                    next_curr.index = curr_temp.index
                                                    next_curr.id = curr.id
                                                    curr_temp.dest = next_curr.src
                                                    i = k
                                                    new_list.append(curr_temp, next_curr)

        for k in range(len(self.list_of_call)):
            e = -1
            if self.list_of_call[k].index == -1:
                for i in range(len(self.building.elevators)):
                    min_time = sys.maxsize
                    t1 = self.building.elevators[i].time()
                    t2 = self.building.elevators[i].time_of_path(self.list_of_call[k].src,
                                                                 self.list_of_call[k].dest)
                    last_call = self.building.elevators[i].list_elev[len(self.building.elevators[i].list_elev) - 1]
                    t3 = self.building.elevators[i].time_of_path(last_call.dest, self.list_of_call[k].src)
                    t123 = t1 + t2 + t3
                    if t123 < min_time:
                        min_time = t123
                        e = i

    def check_path(self, call1, call2, k) -> bool:
        if call1.direction == 1:  # up
            if call1.src <= call2.src:
                return True
            else:
                m = k
                while m > 0:
                    if self.list_of_call[m].id == self.list_of_call[m - 1].id:
                        if self.list_of_call[m - 1].src <= call2.src:
                            self.check_time(self.list_of_call[m - 1], call2, self.list_of_call[m])
                            return True
                    m -= 1
        else:
            if call1.src >= call2.src:
                return True
            else:
                m = k
                while m > 0:
                    if self.list_of_call.Call[m].id == self.list_of_call.Call[m - 1].id:
                        if self.list_of_call.Call[m - 1].src >= call2.src:
                            return True
                    m -= 1

        return False

    def check_time(self, call1, call2, call3) -> int:
        for m in range(len(self.building.elevators)):
            T = self.building.elevators[m].time_of_path(call1.src,
                                                        call2.src)
            T += call1.time
            t = call2.time
            if T >= t:
                call1.index = m
                call2.index = m
                call2.id = call1.id
                call1.dest = call2.src
                call2.dest = call3.src

    # with open(self.output, 'w', newline="") as f:
    #    writer = csv.writer(f)
    #   writer.writerows(self.list_of_call.Call)
