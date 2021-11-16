import csv


class Call:
    calls_list = []
    up_calls = 0
    down_calls = 0

    # status : INIT=0, GOING2SRC=1, GOING2DEST=2, DONE=3;
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _status: int, _who: int):

        self.id = _id
        self.time = _time
        self.src = _src
        self.dest = _dest
        self.status = _status
        self.who = _who

    @classmethod
    def init_data(cls, f_loc2: str):
        calls_list = []  # Create a list which will hold all the calls in the CSV files
        up_calls_counter = 0
        down_calls_counter = 0
        try:
            with open(f_loc2, "rt") as f:
                calls = csv.reader(f)
                for each_call in calls:
                    call = Call(each_call[0], float(each_call[1]), int(each_call[2]), int(each_call[3]),
                                int(each_call[4]), int(each_call[5]))  # creating call
                    calls_list.append(call)
                    if each_call[2] < each_call[3]:
                        up_calls_counter += 1
                    else:
                        down_calls_counter += 1
            return calls_list, up_calls_counter, down_calls_counter
        except FileExistsError as e:
            print(e)

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def set_status(self, n_status: int):
        if 0 <= n_status <= 3:
            self.status = n_status
        else:
            print("Invalid status! Input a number between 0 and 3")

    def get_status(self):
        return self.status

    def get_direction(self):
        return self.direction

    def set_who(self, elevator):
        self.who = elevator

    def get_who(self):
        return self.who

    def __str__(self):
        return "Elevator call" + "," + str(self.get_time()) + "," + str(self.get_src()) \
               + "," + str(self.get_dest()) + "," + str(self.status) + "," + str(self.who)

    def is_on_route(self, call_to_check):
        if self.get_direction() == call_to_check.get_direction() and is_middle(self.get_src(), self.get_dest(),
                                                                               call_to_check.get_src()) and is_middle(
            self.get_src(), self.get_dest(), call_to_check.get_dest()):
            return True
        return False


def is_middle(start, end, x):  # Check and returns a boolean value if x is between start & end
    if end >= x >= start:
        return False
    elif end <= x <= start:
        return True
    return False


def sort_calls_list_a(calls_list: list):
    calls_list.sort(key=lambda x: x.time)


def sort_calls_list_d(calls_list: list):
    calls_list.sort(key=lambda x: x.time, reverse=True)
