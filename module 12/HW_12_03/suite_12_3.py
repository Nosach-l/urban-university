import unittest
import tests_12_2
import tests_12_1


test_suite = unittest.TestSuite()
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)