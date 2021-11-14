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

    def get_min_floor(self):
        return self.minFloor

    def get_max_floor(self):
        return self.maxFloor

    def get_elevators(self):
        return self.elevators


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


class Call:
    # calls_list = [] # static variable,list of calls. instance of Calls.

    # ph1/ph2 = placeholder
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _ph1: int, _ph2: int
                 , direction: int):

class Call:

    # ph1 = placeholder
    # 'who' states which elevator is allocated to the call
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _ph1: int, _who: int):

        self.id = _id
        self.time = _time
        self.src = _src
        self.dest = _dest
        self.ph1 = _ph1
        self.ph2 = _ph2
        if self.src < self.dest:
            self.direction = 1 #UP
        else:
            self.direction = -1 #DOWN

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

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_ph1(self):
        return self.ph1

    def get_ph2(self):
        return self.ph2


class Calls:
    """List of calls"""

    def __init__(self, _calls_list: list):
        self.calls_list = _calls_list

        self.who = _who

    @classmethod
    def init_data(cls, f_loc2: str):
        calls_list = []  # Create a list which will hold all the calls in the CSV files
        try:
            with open(f_loc2, "rt") as f:
                calls = csv.reader(f)
                for each_call in calls:
                    call_vars = ",".join(each_call)
                    call = Call(call_vars[0], float(call_vars[1]), int(call_vars[2]), int(call_vars[3]),
                                int(call_vars[4]), int(call_vars[5]))  # creating call
                    calls_list.append(call)
            return cls(calls_list)
        except FileExistsError as e:
            print(e)


def sort_calls_list_a(calls_list: list):
    calls_list.sort(key=lambda x: x.time)


def sort_calls_list_d(calls_list: list):
    calls_list.sort(key=lambda x: x.time, reverse=True)

# class CallNode:
#
#     # constructor
#     def __init__(self, data: Call, next_call: Call = None):
#         self.data = data
#         if next_call is None:
#             self.next_call = None
#         else:
#             self.next_call = next_call
#
#     @classmethod
#     def not_none_next(cls, data: Call, next_node: Call):
#         return cls(data, next_node)
#
#     def get_data(self):
#         return self.data
#
#     def set_data(self, new_data):
#         self.data = new_data
#
#     def get_next(self):
#         return self.next_node
#
#     def set_next(self, new_next: Call):
#         self.next_node = new_next

        call_list = []  # Create a list which will hold all the calls in the CSV files
        with open(f_loc2, "rt") as f:
            data = csv.reader(f)
            for row in data:
                call_list.append(Call(row[0], float(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])))

