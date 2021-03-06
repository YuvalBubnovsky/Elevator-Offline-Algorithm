import json
import Elevator_Class


class Building:

    def __init__(self, name: str, elevators: list, _minFloor: int, _maxFloor: int):
        """constructor
            :param name: final variable, the name of the building
            :param elevators: list of elevators
            :param _minFloor: minimum floor of this building
            :param _maxFloor: maximum floor of this building
        """
        self.name = name
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.elevators = elevators

    @classmethod
    def init_data(cls, f_loc1: str):
        """loading data from JSON file
            :param f_loc1: name of JSON file to load from
        """
        try:
            with open(f_loc1, "r") as data:
                object_data = json.load(data)
                name = f_loc1.split('/')[3]
                name_final = name.split('.')[0]
                min_floor = object_data["_minFloor"]
                max_floor = object_data["_maxFloor"]
                elevators = [Elevator_Class.Elevator.construct(_elevator) for _elevator in object_data["_elevators"]]
            return cls(name_final, elevators, min_floor, max_floor)
        except FileExistsError as e:
            print(e)

    def get_name(self):
        """:return the name of the building"""
        return self.name

    def get_min_floor(self):
        """:return minimum floor of building"""
        return self.minFloor

    def get_max_floor(self):
        """:return maximum floor of building"""
        return self.maxFloor

    def get_elevators(self):
        """:return: list of the elevators of this building"""
        return self.elevators

