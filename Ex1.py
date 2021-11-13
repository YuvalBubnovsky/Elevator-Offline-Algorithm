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
        try:
            with open(f_loc1, "r") as data:
                object_data = json.load(data)
                min_floor = object_data["_minFloor"]
                max_floor = object_data["_maxFloor"]
                elevators = [Elevator.construct(_elevator) for _elevator in object_data["_elevators"]]
            return cls(elevators, min_floor, max_floor)
        except FileExistsError as e:
            print(e)


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
    # calls_list = [] # static variable,list of calls. instance of Calls.

    # ph1/ph2 = placeholder
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _ph1: int, _ph2: int):
        self.id = _id
        self.time = _time
        self.src = _src
        self.dest = _dest
        self.ph1 = _ph1
        self.ph2 = _ph2

    # # TODO : Need to fix this
    # @classmethod
    # def init_data(self, f_loc2: str):
    #     calls_list_temp = [] # Create a list which will hold all the calls in the CSV files
    #     try:
    #         with open(f_loc2, "rt") as f:
    #             calls = csv.reader(f)
    #             for each_call in calls:
    #                 call = Call(*each_call)
    #                 calls_list_temp.append(call)
    #         self.calls_list = Calls(calls_list_temp)
    #         return
    #     except FileExistsError as e:
    #         print(e)


class Calls:
    """List of calls"""

    def __init__(self, _calls_list: list):
        self.calls_list = _calls_list

    @classmethod
    def init_data(cls, f_loc2: str):
        calls_list = []  # Create a list which will hold all the calls in the CSV files
        try:
            with open(f_loc2, "rt") as f:
                calls = csv.reader(f)
                for each_call in calls:
                    call_vars = ",".join(each_call)
                    call = Call(call_vars)  # creating call
                    calls_list.append(call)
            return cls(calls_list)
        except FileExistsError as e:
            print(e)



