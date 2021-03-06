class CallForElevator:
    def __init__(self, rows):
        self.str = str(rows[0])  # string : Elevator call
        self.time = float(rows[1])  # the time
        self.src = int(rows[2])  # source floor
        self.dest = int(rows[3])  # dest floor
        self.status = int(rows[4])  # status of the elevator
        self.index = int(rows[5])  # number of the elevator
        self.id = -1  # id of Call for Elevator , help us to know which calls in the same path
        self.src_demo = int(rows[2])  # the demo src for the call of elevator
        self.dest_demo = int(rows[3])  # the demo dest for the call of elevator

    def __iter__(self):
        return iter([self.str, self.time, self.src, self.dest, self.status, self.index])

    def __str__(self):
        return str(self.str) + " " + str(self.time) + " " + str(self.src) + " " + str(self.dest) + " " \
               + str(self.status) + " " + str(self.index) + " " + str(self.id) + ", "

    def direction(self) -> int:  # 1=up , 0=down
        if self.src < self.dest:
            return 1
        else:
            return -1
