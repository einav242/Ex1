
class CallForElevator:
    def __init__(self, rows):
        self.str = str(rows[0])  # string : Elevator call
        self.time = float(rows[1])  # the time
        self.src = int(rows[2])   # source floor
        self.dest = int(rows[3])  # dest floor
        self.status = int(rows[4])  # status of the elevator
        self.index = int(rows[5])  # index of the elevator

    def __iter__(self):
        return iter([self.str, self.time, self.src, self.dest,self.status, self.index])