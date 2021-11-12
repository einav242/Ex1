

class Elevators:
    def __init__(self, di):
        self._id = di["_id"]
        self._speed = di["_speed"]  # speed of the elevator
        self._maxFloor = di["_maxFloor"]  # max_floor
        self._minFloor = di["_minFloor"]  # min_floor
        self._closeTime = di["_closeTime"]  # close time
        self._openTime = di["_openTime"]  # open time
        self._startTime = di["_startTime"]  # startTime
        self._stopTime = di["_stopTime"]   # stopTime

