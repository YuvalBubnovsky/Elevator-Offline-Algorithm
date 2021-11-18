# Global imports
import unittest

# Local imports
import Ex1
import Building_Class
import Call_Class
import Elevator_Class


class TestCall(unittest.TestCase):
    ele = Elevator_Class.Elevator(0, 1, -2, 10, 3, 3, 2, 2)
    ele2 = Elevator_Class.Elevator(1, 1, -1, 9, 2, 1, 2, 2)

    call_1 = Call_Class.Call(0, 1, 0, 1, 0, ele)
    call_2 = Call_Class.Call(1, 22.1, -2, 10, 0, ele)
    call_3 = Call_Class.Call(2, 53.5, 9, -1, 0, ele)

    def test_get_id(self):
        self.assertEqual(self.call_1.get_id(), 0, "failed call 1 id check")
        self.assertEqual(self.call_2.get_id(), 1, "failed call 2 id check")
        self.assertEqual(self.call_3.get_id(), 2, "failed call 3 id check")

    def test_get_time(self):
        self.assertEqual(self.call_1.get_time(), 1, "failed call 1 time check")
        self.assertEqual(self.call_2.get_time(), 22.1, "failed call 2 time check")
        self.assertEqual(self.call_3.get_time(), 53.5, "failed call 3 time check")

    def test_get_src(self):
        self.assertEqual(self.call_1.get_src(), 0, "failed call 1 source check")
        self.assertEqual(self.call_2.get_src(), -2, "failed call 2 source check")
        self.assertEqual(self.call_3.get_src(), 9, "failed call 3 source check")

    def test_get_dest(self):
        self.assertEqual(self.call_1.get_dest(), 1, "failed call 1 destination check")
        self.assertEqual(self.call_2.get_dest(), 10, "failed call 2 destination check")
        self.assertEqual(self.call_3.get_dest(), -1, "failed call 3 destination check")

    def test_get_who(self):
        self.assertEqual(self.call_1.get_who(), self.ele, "failed call 1 allocation check")
        self.assertEqual(self.call_2.get_who(), self.ele, "failed call 2 allocation check")
        self.assertEqual(self.call_3.get_who(), self.ele, "failed call 3 allocation check")

    def test_set_who(self):
        self.call_1.set_who(self.ele2)
        self.assertEqual(self.call_1.get_who(), self.ele2, "failed set allocation check")
        self.call_2.set_who(self.ele2)
        self.assertEqual(self.call_2.get_who(), self.ele2, "failed failed set allocation check")
        self.call_3.set_who(self.ele2)
        self.assertEqual(self.call_3.get_who(), self.ele2, "failed set allocation check")


if __name__ == '__main__':
    unittest.main()