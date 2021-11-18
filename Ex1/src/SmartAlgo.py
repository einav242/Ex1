import csv
import sys

from Building import Building
from ListOfCallForElevator import ListOfCallForElevator


class SmartElevatorAlgo:

    def __init__(self, building, calls, output):
        self.building = Building(building)
        self.list_of_call = ListOfCallForElevator(calls).Call
        self.output = output

    def __iter__(self):
        return iter([self.building, self.list_of_call, self.output])

    def elevator_assignment(self):
        ID = 0  # Initial value of ID
        if self.building.number_of_elevator == 1:  # if we have one elevator in the building
            for k in range(len(self.list_of_call)):  # all the Calls will get the same elevator
                self.list_of_call[k].index = 0
                self.list_of_call[k].id = 0

        else:  # in the building have more then one elevator
            for j in range(len(self.list_of_call)):  # j run of all the Calls
                curr = self.list_of_call[j]  # curr = call j in the list
                if curr.id == -1:  # if the call curr is not in any path
                    curr.id = ID  # Gives value to curr id
                    ID += 1  # changes id value
                    i = j  # we dont want cheng j
                    for k in range(j + 1, len(self.list_of_call)):  # k run of all the calls between j+1 to the rest
                        curr_temp = self.list_of_call[i]
                        next_curr = self.list_of_call[k]
                        if next_curr.id == -1 and curr_temp.direction() == next_curr.direction() \
                                and curr_temp.dest_demo == next_curr.dest_demo:
                            if self.check_path(curr_temp, next_curr, k):
                                # call next_curr and curr_temp did not get elevator
                                if next_curr.index == -1 and curr_temp.index == -1:
                                    e = -1
                                    min_call = sys.maxsize
                                    # m run of all the elevator in the building
                                    for m in range(len(self.building.elevators)):
                                        T = self.building.elevators[m].time_of_path(curr_temp.src_demo,
                                                                                    next_curr.src_demo)
                                        T += curr_temp.time
                                        t = next_curr.time
                                        if T >= t:  # if we dont pass src floor of next_curr
                                            # choose the elevator with the shorter list
                                            if len(self.building.elevators[m].list_elev) < min_call:
                                                e = m
                                                min_call = len(self.building.elevators[m].list_elev)
                                    if e != -1:  # if we found the right elevator
                                        curr_temp.index = e
                                        next_curr.index = e
                                        next_curr.id = curr_temp.id
                                        curr_temp.dest_demo = next_curr.src_demo
                                        i = k
                                        # insert the calls to the elevator list
                                        self.building.elevators[e].list_elev.append(curr_temp)
                                        self.building.elevators[e].list_elev.append(next_curr)
                                # call next_curr did not assignment elevator and curr_temp got elevator
                                elif curr_temp.index != -1 and next_curr.index == -1:
                                    e = curr_temp.index # the elevator that allocated to curr_temp
                                    T = self.building.elevators[e].time_of_path(curr_temp.src_demo, next_curr.src_demo)
                                    T += curr_temp.time
                                    t = next_curr.time
                                    if T >= t: # if we dont pass src floor of next_curr
                                        next_curr.index = e
                                        next_curr.id = curr_temp.id
                                        # change the dest of curr_temp to be the src of next_curr
                                        curr_temp.dest_demo = next_curr.src_demo
                                        i = k
                                        # where curr_temp in the elevator list
                                        ind = self.building.elevators[e].list_elev.index(curr_temp)
                                        # put next_curr after curr_temp in elevator list
                                        self.building.elevators[e].list_elev.insert(ind + 1, next_curr)
                                # call next_curr and curr_temp get the same elevator
                                elif next_curr != -1 and curr_temp != -1:
                                    i = k  # now i = k and we chek the next calls between i to new k

# all the calls in the list that did not get a elevator now we will assignment them a elevator
# the elevator that we assignment is the elevator with the min calls .
        for k in range(len(self.list_of_call)):
            e = -1
            min_call = sys.maxsize
            if self.list_of_call[k].index == -1:  # if we dont allocated elevator to this call
                for i in range(len(self.building.elevators)):
                    if len(self.building.elevators[i].list_elev) < min_call:
                        min_call = len(self.building.elevators[i].list_elev)
                        e = i
                self.list_of_call[k].index = e
                self.building.elevators[e].list_elev.append(self.list_of_call[k])
        self.write_calls()  # write the output file

# check_path - return true or false if call1 and call2 can up / down together
    def check_path(self, call1, call2, k) -> bool:
        if call1.direction == 1:  # up
            if call1.src_demo <= call2.src_demo:
                return True
            if call1.index != -1:  # if call1 got elevator
                m = k
                while m > 0:  # we will chek the rest calls with the same id like call1
                    if call1.id == self.list_of_call[m - 1].id:
                        if self.list_of_call[m - 1].src_demo <= call2.src_demo:
                            if self.check_time(self.list_of_call[m - 1], call2, call1.index):
                                return True
                    m -= 1
            return False
        else:  # down
            if call1.src_demo >= call2.src_demo:
                return True
            if call1.index != -1:  # if call1 got elevator
                m = k
                while m > 0:  # we will chek the rest calls with the same id like call1
                    if call1.id == self.list_of_call[m - 1].id:
                        if self.list_of_call[m - 1].src_demo >= call2.src_demo:
                            if self.check_time(self.list_of_call[m - 1], call2, call1.index):
                                return True
                    m -= 1
            return False

# return true if elevator of call1 and call2 in the same path if that do allocated
# elevator e to call2 .
    def check_time(self, call1, call2, e) -> bool:
        T = self.building.elevators[e].time_of_path(call1.src_demo, call2.src_demo)
        T += call1.time
        t = call2.time
        if T >= t:
            # where call1 in the elevator list
            ind = self.building.elevators[e].list_elev.index(call1)
            call2.index = e
            call2.id = call1.id
            # change the dest of call1 to be the src of call2 and the dest of call1 to be the dest of call2
            temp = call1.dest_demo
            call1.dest_demo = call2.src_demo
            call2.dest_demo = temp
            # put call2 after call1 in elevator list
            self.building.elevators[e].list_elev.insert(ind + 1, call2)
            return True

    def write_calls(self):
        with open(self.output, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.list_of_call)
