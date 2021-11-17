import Call_Class


class Elevator:

    def __init__(self, _id: int, _speed: int, _minFloor: int, _maxFloor: int, _closeTime: float, _openTime: float,
                 _startTime: float, _stopTime: float):
        """constructor
            :param _id: id of elevator
            :param _speed: speed of elevator (floor per second)
            :param _startTime: acceleration time
            :param _stopTime: slowing down time
            :param _maxFloor: the highest floor which the elevator can reach
            :param _minFloor: the lowest floor which the elevator can reach
            :param _closeTime: time takes the doors to close
            :param _openTime: time takes the doors to open
        """
        self.id = _id
        self.speed = _speed
        self.minFloor = _minFloor
        self.maxFloor = _maxFloor
        self.closeTime = _closeTime
        self.openTime = _openTime
        self.startTime = _startTime
        self.stopTime = _stopTime
        self.currState = 0  # all elevators starts in level position
        self.currPos = 0
        self.currTime = 0.0

    # Helper function to create the Elevator object while in the loop of reading the JSON file parameters
    @classmethod
    def construct(cls, data):
        """construct the elevator with all its attributes"""
        return cls(**data)

    """get and set method of each attribute of elevator"""
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

    def set_pos(self, floor):
        self.currPos = floor

    def get_pos(self):
        return self.currPos

    def get_state(self):
        return self.currState

    # def get_penalty_time(self):
    #     return self.startTime + self.stopTime + self.openTime + self.closeTime

    def set_time(self, time):
        self.currTime = time

    def get_time(self):
        return self.currTime

    def __str__(self):
        """:return return string which represent the elevator"""
        return "" + str(self.id) + "," + str(self.speed) + "," + str(self.minFloor) + "," \
               + str(self.maxFloor) + "," + str(self.closeTime) + "," + str(self.openTime) \
               + "," + str(self.startTime) + "," + str(self.stopTime) + "," + str(self.get_pos()) \
               + "," + str(self.currState)

    def travel_time(self, Call: Call_Class) -> float:
        """ compute the time that takes the elevator to travel from source to destination

        :param Call:
        :return: float
        """
        return float(self.get_close_time() + self.get_start_time() + (abs(Call.get_src() - Call.get_dest()) / (
            self.get_speed())) + self.get_stop_time() + self.get_open_time())


    def time_a_to_b(self, src_floor: int, dest_floor: int) -> float:
        """ compute the time that takes the elevator to travel from a to b

        :param src_floor:
        :param dest_floor:
        :return:
        """
        return float(self.get_close_time() + self.get_start_time() + (abs(src_floor - dest_floor) / (
            self.get_speed())) + self.get_stop_time() + self.get_open_time())
