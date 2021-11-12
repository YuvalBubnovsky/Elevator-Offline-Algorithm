import json


# Building class to hold building parameters and our elevators
class Building:

    def __init__(self, elevators, _minFloor: int, _maxFloor: int):
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.elevators = elevators

    @classmethod
    def init_data(cls, f_loc1: str):
        with open(f_loc1, "r") as data:
            objectData = json.load(data)
            min_floor = objectData["_minFloor"]
            max_floor = objectData["_maxFloor"]
            elevators = [Elevator.construct(_elevator) for _elevator in objectData["_elevators"]]
        return cls(elevators, min_floor, max_floor)


# Elevator class, initialization from JSON file
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

    @classmethod
    def construct(cls, data):
        return cls(**data)
