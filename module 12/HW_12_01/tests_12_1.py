import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner = Runner('example')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('example')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('example')
        runner2 = Runner('example2')
        for i in range(10):
            runner2.walk()
            runner.run()
        self.assertNotEqual(runner2.distance, runner.distance)


if __name__ == '__main__':
    unittest.main()
