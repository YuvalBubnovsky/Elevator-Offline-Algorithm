import sys
import Building_Class
import Elevator_Class
import Call_Class



def init():
    Building_Class.Building.init_data(sys.argv[1])
    call_list = Call_Class.Call.init_data(sys.argv[2])
    allocate(sys.argv[3], call_list)

def allocate(f_loc3: str, calls):



if __name__ == "__Ex1__":
    init()
