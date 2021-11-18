# Global imports
import unittest

# Local imports
import Ex1
import Building_Class
import Call_Class
import Elevator_Class


class TestBuilding(unittest.TestCase):
    ele0 = Elevator_Class.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    ele1 = Elevator_Class.Elevator(2, 5, -10, 100, 2, 2, 1, 1)
    ele2 = Elevator_Class.Elevator(1, 2.5, -5, 40, 2, 2, 1, 1)
    ele3 = Elevator_Class.Elevator(3, 3, -4, 20, 3, 3, 2, 2)
    ele_list_1 = [ele1]
    ele_list_2 = [ele0, ele1, ele2, ele3]
    ele_list_3 = [ele0, ele2]
    building_1 = Building_Class.Building("building 1", ele_list_1, -2, 10)
    building_2 = Building_Class.Building("building 2", ele_list_2, -10, 100)
    building_3 = Building_Class.Building("building 3", ele_list_3, -5, 40)

    def test_get_name(self):
        self.assertEqual(self.building_1.get_name(), "building 1", "failed building 1 name check")
        self.assertEqual(self.building_2.get_name(), "building 2", "failed building 1 name check")
        self.assertEqual(self.building_3.get_name(), "building 3", "failed building 1 name check")

    def test_get_min_floor(self):
        self.assertEqual(self.building_1.get_min_floor(), -2, "failed building 1 min_floor check")
        self.assertEqual(self.building_2.get_min_floor(), -10, "failed building 2 min_floor check")
        self.assertEqual(self.building_3.get_min_floor(), -5, "failed building 3 min_floor check")

    def test_get_max_floor(self):
        self.assertEqual(self.building_1.get_max_floor(), 10, "failed building 1 max_floor check")
        self.assertEqual(self.building_2.get_max_floor(), 100, "failed building 2 max_floor check")
        self.assertEqual(self.building_3.get_max_floor(), 40, "failed building 3 max_floor check")

    def test_get_elevators(self):
        self.assertEqual(self.building_1.get_elevators(), self.ele_list_1, "failed building 1 get_elevators check")
        self.assertEqual(self.building_2.get_elevators(), self.ele_list_2, "failed building 2 get_elevators check")
        self.assertEqual(self.building_3.get_elevators(), self.ele_list_3, "failed building 3 get_elevators check")


if __name__ == '__main__':
    unittest.main()
