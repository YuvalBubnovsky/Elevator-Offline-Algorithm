import sys
import Building_Class
import Elevator_Class
import Call_Class
import csv
import math

"""written by Yuval Bubonvsky and Itamar Kraitman"""

def init():
    """ initializing the arguments needed to run the program"""
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
    allocate("results.csv", call_list[0], building.elevators, up_calls, down_calls)


def allocate(f_loc3: str, calls: list, elevators: list, up_total: int, down_total: int):
    """ allocating elevator for each call
        :param f_loc3: name of csv file to write to
        :param calls: list of calls
        :param elevators: list of elevators
        :param up_total: how many up calls are in total
        :param down_total: how many down calls are in total
    """
    ele_list = []  # list of elevators
    if len(elevators) == 1:
        for call in calls:
            call.who = 0
        # if up_total > down_total:  # more up calls than down calls
    elif len(elevators) % 2 == 0:  # in case number of elevators is even
        for call in calls:
            if call.src > call.dest:  # up call
                for i in range(0, int(len(elevators) / 2)):
                    ele_list.append(elevators[i])
                call.who = find_closest(call=call, elevators=ele_list)
            else:
                for i in range(int(len(elevators) / 2), int(len(elevators))):
                    ele_list.append(elevators[i])
                call.who = find_closest(call=call, elevators=ele_list)
    else:  # in case number of elevators is odd
        if up_total > down_total:  # more up calls than down calls
            for call in calls:
                if call.src > call.dest:  # up call
                    for i in range(0, math.floor(len(elevators) / 2) + 1):
                        ele_list.append(elevators[i])
                    call.who = find_closest(call=call, elevators=ele_list)
                else:  # down call
                    for i in range(int(len(elevators) / 2) + 1, int(len(elevators))):
                        ele_list.append(elevators[i])
                    call.who = find_closest(call=call, elevators=ele_list)
        else:  # more down calls then up calls
            for call in calls:
                if call.src > call.dest:  # up call
                    for i in range(0, math.floor(int(len(elevators) / 2) + 1)):
                        ele_list.append(elevators[i])
                        call.who = find_closest(call=call, elevators=ele_list)
                    else:  # down call
                        for i in range(int(len(elevators) / 2) + 1, int(len(elevators))):
                            elevators.append(elevators[i])
                        call.who = find_closest(call=call, elevators=ele_list)
    write_csv(f_loc3, calls)


def find_closest(call: Call_Class.Call, elevators: list) -> int:
    """finding the closest elevator for a call source with respect to current position and time
        :param call: call to allocate elevator to
        :param elevators: list of elevators
        :return id of closest elevators
    """
    closest: Elevator_Class.Elevator = elevators[0]
    for elevator in elevators:
        if elevator.currPos == call.src:
            return elevator.id  # in case elevator is in source position
        elif (abs(elevator.currPos - call.src) < abs(closest.currPos - call.src)) | \
                (elevator.time_a_to_b(elevator.currPos, call.src) < closest.time_a_to_b(closest.currPos, call.src)):
            closest = elevator
    return closest.id


def write_csv(file: str, calls: list):
    """writing csv file of calls from calls list
        :param file: name of the file to write to
        :param calls: list of calls
    """
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
