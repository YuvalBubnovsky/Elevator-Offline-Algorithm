# Global imports
import unittest

# Local imports
import Ex1
import Building_Class
import Call_Class
import Elevator_Class


class TestElevator(unittest.TestCase):
    ele0 = Elevator_Class.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    ele1 = Elevator_Class.Elevator(1, 5, -10, 100, 2, 2, 1, 1)
    ele2 = Elevator_Class.Elevator(2, 2.5, -5, 40, 2, 2, 1, 1)
    ele3 = Elevator_Class.Elevator(3, 3, -4, 20, 3, 3, 2, 2)

    def test_get_id(self):
        self.assertEqual(self.ele0.get_id(), 0, "failed elevator 0 id check")
        self.assertEqual(self.ele1.get_id(), 1, "failed elevator 1 id check")
        self.assertEqual(self.ele2.get_id(), 2, "failed elevator 2 id check")
        self.assertEqual(self.ele3.get_id(), 3, "failed elevator 3 id check")

    def test_get_speed(self):
        self.assertEqual(self.ele0.get_speed(), 1, "failed elevator 0 speed check")
        self.assertEqual(self.ele1.get_speed(), 5, "failed elevator 1 speed check")
        self.assertEqual(self.ele2.get_speed(), 2.5, "failed elevator 2 speed check")
        self.assertEqual(self.ele3.get_speed(), 3, "failed elevator 3 speed check")

    def test_get_min_floor(self):
        self.assertEqual(self.ele0.get_min_floor(), -2, "failed elevator 0 min_floor check")
        self.assertEqual(self.ele1.get_min_floor(), -10, "failed elevator 1 min_floor check")
        self.assertEqual(self.ele2.get_min_floor(), -5, "failed elevator 2 min_floor check")
        self.assertEqual(self.ele3.get_min_floor(), -4, "failed elevator 3 min_floor check")

    def test_get_max_floor(self):
        self.assertEqual(self.ele0.get_max_floor(), 10, "failed elevator 0 max_floor check")
        self.assertEqual(self.ele1.get_max_floor(), 100, "failed elevator 1 max_floor check")
        self.assertEqual(self.ele2.get_max_floor(), 40, "failed elevator 2 max_floor check")
        self.assertEqual(self.ele3.get_max_floor(), 20, "failed elevator 3 max_floor check")

    def test_get_close_time(self):
        self.assertEqual(self.ele0.get_close_time(), 3, "failed elevator 0 close_time check")
        self.assertEqual(self.ele1.get_close_time(), 2, "failed elevator 1 close_time check")
        self.assertEqual(self.ele2.get_close_time(), 2, "failed elevator 2 close_time check")
        self.assertEqual(self.ele3.get_close_time(), 3, "failed elevator 3 close_time check")

    def test_get_open_time(self):
        self.assertEqual(self.ele0.get_open_time(), 3, "failed elevator 0 open_time check")
        self.assertEqual(self.ele1.get_open_time(), 2, "failed elevator 1 open_time check")
        self.assertEqual(self.ele2.get_open_time(), 2, "failed elevator 2 open_time check")
        self.assertEqual(self.ele3.get_open_time(), 3, "failed elevator 3 open_time check")

    def test_get_start_time(self):
        self.assertEqual(self.ele0.get_start_time(), 2, "failed elevator 0 start_time check")
        self.assertEqual(self.ele1.get_start_time(), 1, "failed elevator 1 start_time check")
        self.assertEqual(self.ele2.get_start_time(), 1, "failed elevator 2 start_time check")
        self.assertEqual(self.ele3.get_start_time(), 2, "failed elevator 3 start_time check")

    def test_get_stop_time(self):
        self.assertEqual(self.ele0.get_stop_time(), 2, "failed elevator 0 stop_time check")
        self.assertEqual(self.ele1.get_stop_time(), 1, "failed elevator 1 stop_time check")
        self.assertEqual(self.ele2.get_stop_time(), 1, "failed elevator 2 stop_time check")
        self.assertEqual(self.ele3.get_stop_time(), 2, "failed elevator 3 stop_time check")

    def test_get_pos(self):
        self.assertEqual(self.ele0.get_pos(), 0, "failed elevator 0 position check")
        self.assertEqual(self.ele1.get_pos(), 0, "failed elevator 1 position check")
        self.assertEqual(self.ele2.get_pos(), 0, "failed elevator 2 position check")
        self.assertEqual(self.ele3.get_pos(), 0, "failed elevator 3 position check")

    def test_set_pos(self):
        self.ele0.set_pos(2)
        self.assertEqual(self.ele0.get_pos(), 2, "failed elevator 0  set position check")
        self.ele1.set_pos(14)
        self.assertEqual(self.ele1.get_pos(), 14, "failed elevator 1 set position check")
        self.ele2.set_pos(38)
        self.assertEqual(self.ele2.get_pos(), 38, "failed elevator 2 set position check")
        self.ele3.set_pos(-3)
        self.assertEqual(self.ele3.get_pos(), -3, "failed elevator 3 set position check")


if __name__ == '__main__':
    unittest.main()
