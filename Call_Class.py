import csv


class Call:
    calls_list = []

    # ph1/ph2 = placeholder
    def __init__(self, _id: str, _time: float, _src: int, _dest: int, _ph1: int, _ph2: int
                 , direction: int):

        self.id = _id
        self.time = _time
        self.src = _src
        self.dest = _dest
        self.ph1 = _ph1
        self.ph2 = _ph2
        self.direction = 0
        if self.src < self.dest:
            self.direction = 1  # UP
        else:
            self.direction = -1  # DOWN

    @classmethod
    def init_data(cls, f_loc2: str):
        calls_list = []  # Create a list which will hold all the calls in the CSV files
        try:
            with open(f_loc2, "rt") as f:
                calls = csv.reader(f)
                for each_call in calls:
                    call_vars = ",".join(each_call)
                    call = Call(call_vars[0], float(call_vars[1]), int(call_vars[2]), int(call_vars[3]),
                                int(call_vars[4]), int(call_vars[5]), 0)  # creating call
                    calls_list.append(call)
            return calls_list
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

    def get_ph1(self):
        return self.ph1

    def get_ph2(self):
        return self.ph2


def sort_calls_list_a(calls_list: list):
    calls_list.sort(key=lambda x: x.time)


def sort_calls_list_d(calls_list: list):
    calls_list.sort(key=lambda x: x.time, reverse=True)
