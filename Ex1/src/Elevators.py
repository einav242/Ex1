from Ex1.src.CallForElevator import CallForElevator


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
        self.list_elev = []

    def time(self) -> float:  # the time of all the call of this elevator
        total_time = 0
        if len(self.list_elev) > 0:
            floor_start = self.list_elev[0].src
            total_time = self._speed * floor_start + self._stopTime + self._startTime + self._openTime + self._closeTime
            for k in range(len(self.list_elev)):
                time = self.time_of_path(self.list_elev[k].src, self.list_elev[k].dest)
                total_time = total_time + time

        return total_time

    def time_of_path(self, src, dest) -> float:
        floor = abs(src - dest)
        time = self._speed * floor + self._stopTime + self._startTime + self._openTime + self._closeTime
        return time

    def __iter__(self):
        for k in range(len(self.list_elev)):
            return iter(self.list_elev(k))

    def __str__(self):
        st = ""
        for k in range(len(self.list_elev)):
            st += str(self.list_elev[k])
        return st
