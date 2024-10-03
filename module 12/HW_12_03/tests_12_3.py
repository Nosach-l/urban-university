import unittest
from runner_and_tournament import Runner, Tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner('example')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner('example')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner = Runner('example')
        runner2 = Runner('example2')
        for i in range(10):
            runner2.walk()
            runner.run()
        self.assertNotEqual(runner2.distance, runner.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race1(self):
        test_race = Tournament(90, self.runner1, self.runner3).start()
        self.all_results[1] = test_race
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race2(self):
        test_race = Tournament(90, self.runner2, self.runner3).start()
        self.all_results[2] = test_race
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_race3(self):
        test_race = Tournament(90, self.runner1, self.runner2, self.runner3).start()
        self.all_results[3] = test_race
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')


if __name__ == '__main__':
    unittest.main()
