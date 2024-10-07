import unittest
from rt_with_exceptions import Runner
import logging


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner('Вася', -5)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk", выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    def test_run(self):
        try:
            runner = Runner(2, 5)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run", выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    def test_challenge(self):
        runner = Runner('example')
        runner2 = Runner('example2')
        for i in range(10):
            runner2.walk()
            runner.run()
        self.assertNotEqual(runner2.distance, runner.distance)


if __name__ == '__main__':
    unittest.main()




