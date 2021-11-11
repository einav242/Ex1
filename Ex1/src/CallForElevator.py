class CallForElevator:
    def __init__(self, rows):
        self.str = str(rows[0])
        self.time = float(rows[1])
        self.src = int(rows[2])
        self.dest = int(rows[3])
        self.status = int(rows[4])
        self.index = int(rows[5])

    def __iter__(self):
        return iter([self.str, self.time, self.src, self.dest,self.status, self.index])
