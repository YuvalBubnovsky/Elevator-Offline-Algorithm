import json
import csv


# Building class to hold building parameters and our elevators
class Building:

    def __init__(self, elevators, _minFloor: int, _maxFloor: int):
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.elevators = elevators

    @classmethod
    def init_data(cls, f_loc1: str):
        with open(f_loc1, "r") as data:
            object_data = json.load(data)
            min_floor = object_data["_minFloor"]
            max_floor = object_data["_maxFloor"]
            elevators = [Elevator.construct(_elevator) for _elevator in object_data["_elevators"]]
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

    # Helper function to create the Elevator object while in the loop of reading the JSON file parameters
    @classmethod
    def construct(cls, data):
        return cls(**data)


class Call:

    # ph1 = placeholder
    # 'who' states which elevator is allocated to the call
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _ph1: int, _who: int):
        self.id = _id
        self.time = _time
        self.src = _src
        self.dest = _dest
        self.ph1 = _ph1
        self.who = _who

    @classmethod
    def init_data(cls, f_loc2: str):
        call_list = []  # Create a list which will hold all the calls in the CSV files
        with open(f_loc2, "rt") as f:
            data = csv.reader(f)
            for row in data:
                call_list.append(Call(row[0], float(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])))

