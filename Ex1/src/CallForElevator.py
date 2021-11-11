class CallForElevator:
    def __init__(self, rows):
        self.str = rows[0]
        self.time = rows[1]
        self.src = rows[2]
        self.dest = rows[3]
        self.index = rows[5]

    def __iter__(self):
        return iter([self.str, self.time, self.src, self.dest, self.index])


