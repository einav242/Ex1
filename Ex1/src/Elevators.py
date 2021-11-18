
class Elevators:
    def __init__(self, di):
        self._id = int(di["_id"])
        self._speed = float(di["_speed"])  # speed of the elevator
        self._maxFloor = int(di["_maxFloor"])  # max_floor
        self._minFloor = int(di["_minFloor"])  # min_floor
        self._closeTime = float(di["_closeTime"])  # close time
        self._openTime = float(di["_openTime"])  # open time
        self._startTime = float(di["_startTime"])  # startTime
        self._stopTime = float(di["_stopTime"])  # stopTime
        self.list_elev = []  # list of all the call that allocated to this elevator

    # return the time that takes  go to src to dest
    def time_of_path(self, src, dest) -> float:
        floor = abs(src - dest)
        if floor != 0:
            time = floor / self._speed + self._stopTime + self._startTime + self._openTime + self._closeTime
            return time
        else:
            return 0

    def __iter__(self):
        for k in range(len(self.list_elev)):
            return iter(self.list_elev(k))

    def __str__(self):
        st = ""
        for k in range(len(self.list_elev)):
            st += str(self.list_elev[k])
        return st