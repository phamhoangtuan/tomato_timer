from main import TomatoTimer
import unittest


class TestMain(unittest.TestCase):
    def test_default_init_class(self):
        timer = TomatoTimer()
        self.assertEqual(timer.pomodoro_time, 25)
        self.assertEqual(timer.short_break_time, 5)
        self.assertEqual(timer.long_break_time, 10)
        self.assertEqual(timer.target_pomodoro, 10)

    def test_custom_init_class(self):
        timer = TomatoTimer(20, 3, 15, 4)
        self.assertEqual(timer.pomodoro_time, 20)
        self.assertEqual(timer.short_break_time, 3)
        self.assertEqual(timer.long_break_time, 15)
        self.assertEqual(timer.target_pomodoro, 4)

    # TODO: write test for calling class methods


if __name__ == '__main__':
    unittest.main()
