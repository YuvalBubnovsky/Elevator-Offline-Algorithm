import sys
import Building_Class
import Elevator_Class
import Call_Class
import csv


def init(argv):
    building = Building_Class.Building.init_data(sys.argv[1])
    call_list = Call_Class.Call.init_data(sys.argv[2])
    allocate(f_loc3=sys.argv[3], calls=call_list, elevators=building.elevators)


def allocate(f_loc3: str, calls, elevators: list):
    # if len(elevators) == 1:
    # TO-DO assign all calls to elevator 1
    for call in calls:
        call.ph1 = 0
    write_csv(f_loc3, calls)


# else:
#     for call in calls:
#         pass


def current_pos(ele: Elevator_Class.Elevator):
    pass


def write_csv(file: str, call: Call_Class.Call):
    try:
        values = [attr for attr in dir(call) if not callable(getattr(call, attr)) and not attr.startswith("__")]
        with open(file, "w") as results:
            writer = csv.writer(results, dialect='excel')
            writer.writerows(values)
    except Exception as e:
        print(e)
        print("error has occurred")


if __name__ == "__main__":
    init(sys.argv[0])
