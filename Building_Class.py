import json
import Elevator_Class


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
                elevators = [Elevator_Class.Elevator.construct(_elevator) for _elevator in object_data["_elevators"]]
            return cls(elevators, min_floor, max_floor)
        except FileExistsError as e:
            print(e)

    def get_min_floor(self):
        return self.minFloor

    def get_max_floor(self):
        return self.maxFloor

    def get_elevators(self):
        return self.elevators
