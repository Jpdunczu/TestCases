import unittest
from hw1 import *

class TestFnTester(unittest.TestCase):
	def setUp(self):
		def f(a,b):
			return b/a
		self.case = (f, [1,2], 2)
		self.not_a_tuple = [f,[1,2],2]
		self.not_len_3 = (f,[1,2])
		self.first_not_function = ('f',[1,2],2)
		self.second_not_list = (f,'1,2',2)
		self.wrong_return_value = (f,[1,2],3)
		self.suite = [self.case, self.case, self.case, self.case]
		self.suite_not_list = (self.case, self.case)
		self.suite_one_not_correct = [self.case, self.case, self.case, self.not_len_3]
		self.suite_one_must_fail = [self.case, self.case, self.case, self.wrong_return_value]
		
		
		
		
		self.case_exception = (f,[0,2],2)
		
		def tearDown(self):
			self.case_exception.dispose()
			self.case_exception = None
			self.suite_one_must_fail.dispose()
			self.suite_one_must_fail = None
			self.suite_one_not_correct.dispose()
			self.suite_one_not_correct = None
			self.suite_not_list.dispose()
			self.suite_not_list = None
			self.suite.dispose()
			self.suite = None
			self.wrong_return_value.dispose()
			self.wrong_return_value = None
			self.case.dispose()
			self.case = None
			self.not_a_tuple.dispose()
			self.not_a_tuple = None
			self.not_len_3.dispose()
			self.not_len_3 = None
			self.first_not_function.dispose()
			self.first_not_function = None
			self.second_not_list.dispose()
			self.second_not_list = None
			
	#####################
	# correct_test_format
	#####################
	def test_correct_test_format(self):
		"""Test 1: correct_test_format() works under normal conditions."""
		self.assertTrue(correct_test_format(self.case)) 
		
	def test_not_a_tuple(self):
		"""Test 2: correct_test_format() returns False if not passed a 'tuple' type."""
		self.assertFalse(correct_test_format(self.not_a_tuple))
	
	def test_not_len_3(self):
		"""Test 3: correct_test_format() returns False if parameter length != 3."""
		self.assertFalse(correct_test_format(self.not_len_3))
		
	def test_first_not_function(self):
		"""Test 4: correct_test_format() returns False if first element is not a callable function."""
		self.assertFalse(correct_test_format(self.first_not_function))
		
	def test_second_not_list(self):
		"""Test 5: correct_test_format() returns False if second element is not a 'list' type."""
		self.assertFalse(correct_test_format(self.second_not_list))
		
	######################
	# correct_suite_format
	######################
	def test_correct_suite_format(self):
		"""Test 1: correct_suite_format() works under normal conditions."""
		self.assertTrue(correct_suite_format(self.suite))
		
	def test_suite_not_a_list(self):
		"""Test 2: correct_suite_format() returns False if parameter is not a 'list' type."""
		self.assertFalse(correct_suite_format(self.suite_not_list))
		
	def test_suite_one_not_correct(self):
		"""Test 3: correct_suite_format() returns False if a test case in the suite is not of the correct format."""
		self.assertFalse(correct_suite_format(self.suite_one_not_correct))
		
	##########
	# run_test
	##########
	def test_run_test(self):
		"""Test 1: run_test() works under normal conditions."""
		self.assertTrue(run_test(self.case))
		
	def test_wrong_return_value(self):
		"""Test 2: run_test() returns False when a test does not return the expected value."""
		self.assertFalse(run_test(self.wrong_return_value))
		
	def test_exception_raised(self):
		"""Test 3: run_test() correct parameters but throws an exception."""
		with self.assertRaises(ZeroDivisionError):
			run_test(self.case_exception)
			
	def test_not_correct_format(self):
		"""Test 4: run_test() returns False when parameter is not correct format."""
		self.assertFalse(run_test(self.first_not_function))
		
	###########
	# run_suite
	###########
	def test_run_suite(self):
		"""Test 1: run_suite() must have at least one pass and one fail."""
		self.assertEqual(run_suite(self.suite_one_must_fail), [3,1])
		
	def test_suite_not_correct_format(self):
		"""Test 2: run_suite() returns False if parameter is not a correct suite format."""
		self.assertFalse(run_suite(self.suite_not_list))
		
if __name__ == '__main__':
	unittest.main(verbosity=2)