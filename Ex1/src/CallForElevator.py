class CallForElevator:
    def __init__(self, rows):
        self._str = rows[0]
        self._time = rows[1]
        self._src = rows[2]
        self._dest = rows[3]
        self._index = rows[5]

    def __iter__(self):
        return iter([self._str, self._time, self._src, self._dest, self._index])
