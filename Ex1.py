import Building_Class
import Elevator_Class
import Call_Class
import sys


def init():
    Building_Class.Building.init_data(sys.argv[1])
    Call_Class.Call.init_data(sys.argv[2])


if __name__ == "__Ex1__":
    init()
