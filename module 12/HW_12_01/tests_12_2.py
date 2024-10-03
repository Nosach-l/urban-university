import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

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

    def test_race1(self):
        test_race = Tournament(90, self.runner1, self.runner3).start()
        self.all_results[1] = {i: runner.name for i, runner in test_race.items()}
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')

    def test_race2(self):
        test_race = Tournament(90, self.runner2, self.runner3).start()
        self.all_results[2] = {i: runner.name for i, runner in test_race.items()}
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')

    def test_race3(self):
        test_race = Tournament(90, self.runner1, self.runner2, self.runner3).start()
        self.all_results[3] = {i: runner.name for i, runner in test_race.items()}
        self.assertTrue(test_race[list(test_race.keys())[-1]] == self.runner3.name, 'Ник всегда должен быть последним')


if __name__ == '__main__':
    unittest.main()
