import sys
import Building_Class
import Elevator_Class
import Call_Class
import csv


def init():
    up_calls = 0
    down_calls = 0
    building = Building_Class.Building.init_data(sys.argv[1])
    call_list = Call_Class.Call.init_data(sys.argv[2])
    try:
        with open(sys.argv[2], "rt") as f:
            calls = csv.reader(f)
            for call in calls:
                if call[2] < call[3]:
                    up_calls += 1
                else:
                    down_calls += 1
    except FileExistsError as e:
        print(e)
    allocate(sys.argv[3], call_list, building.elevators, up_calls, down_calls)


def allocate(f_loc3: str, calls: list, elevators: list, up_total: int, down_total: int):
    if len(elevators) == 1:
        for call in calls:
            call.who = 0
        write_csv(f_loc3, calls)
    elif len(elevators) % 2 == 0:
        pass
    else:


def scanCsv
        pass


# def current_pos(ele: Elevator_Class.Elevator):
#     pass


def write_csv(file: str, calls: list):
    try:
        for i in range(len(calls)):
            calls[i] = calls[i].__dict__.values()
        with open(file, 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerows(calls)
    except Exception as e:
        print(e)
        print("error has occurred")


if __name__ == "__main__":
    init()
