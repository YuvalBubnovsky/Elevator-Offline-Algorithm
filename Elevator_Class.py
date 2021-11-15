class Elevator:

    def __init__(self, _id: int, _speed: int, _minFloor: int, _maxFloor: int, _closeTime: float, _openTime: float,
                 _startTime: float, _stopTime: float):
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime

    # Helper function to create the Elevator object while in the loop of reading the JSON file parameters
    @classmethod
    def construct(cls, data):
        return cls(**data)

    def get_id(self):
        return self.id

    def get_speed(self):
        return self.speed

    def get_min_floor(self):
        return self.minFloor

    def get_max_floor(self):
        return self.maxFloor

    def get_close_time(self):
        return self.closeTime

    def get_open_time(self):
        return self.openTime

    def get_start_time(self):
        return self.startTime

    def get_stop_time(self):
        return self.stopTime
