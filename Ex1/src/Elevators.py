class Elevators:
    def __init__(self, di):
        self._id = di["_id"]
        self._speed = di["_speed"]  # speed of the elevator
        self._maxFloor = di["_maxFloor"]  # max_floor
        self._minFloor = di["_minFloor"]  # min_floor
        self._closeTime = di["_closeTime"]  # close time
        self._openTime = di["_openTime"]  # open time
        self._startTime = di["_startTime"]  # startTime
        self._stopTime = di["_stopTime"]  # stopTime
        self.list_elev = []

    def time(self) -> float:  # the time of all the call of this elevator
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
