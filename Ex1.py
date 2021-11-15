import sys
import Building_Class
import Elevator_Class
import Call_Class
import csv


def init(argv):
    building = Building_Class.Building.init_data(sys.argv[1])
    call_list = Call_Class.Call.init_data(sys.argv[2])
    allocate(sys.argv[3], call_list, building.elevators)


def allocate(f_loc3: str, calls: list, elevators: list):
    # if len(elevators) == 1:
    # TO-DO assign all calls to elevator 1
    for call in calls:
        call.who = 0
    write_csv(f_loc3, calls)


# else:
#     for call in calls:
#         pass


def current_pos(ele: Elevator_Class.Elevator):
    pass


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
    init(sys.argv[0:])
