def correct_test_format(test):
	"""Checks the argument against three criteria, returns True if all tests succeed, false, and prints out the reason, otherwise"""
	if isinstance(test,tuple):
		if isinstance(test[1],list):
			if callable(test[0]):
				return True
			else:
				print('test[0] function not callable')
				return False
		else:
			print('second element not a list')
			return False
	else:
		print('test not a tuple')
		return False

def correct_suite_format(suite):
	"""Checks that the argument passed is a list, then calls another function to check for validity of the elements of the list, returns True if all tests successful, false, and prints out the reason, otherwise."""
	if isinstance(suite,list):
		element = 1
		for tests in suite:
			test = correct_test_format(tests)
			if test:
				element += 1
			else:
				print('test: ', element, ', is not a correct test.')
				return False
		return True
		
def run_test(test):
	"""Checks if the argument passed is a valid test, then checks to make sure the test's function returns the correct result."""
	if correct_test_format(test):
		function = test[0]
		if function() == test[2]:
			return True
		else:
			return False
	else:
		return False
		
def run_suite(suite):
	"""Runs a list of tests, records success and failures of each test, then returns the result of Pass and Fails in a list"""
	testsPassed, testsFailed = 0, 0
	for tests in suite:
		if run_test(tests):
			testsPassed += 1
		else:
			testsFailed += 1
		result = [testsPassed, testsFailed]
	return result
	
def main():
	return

if __name__ == "__main__":
	main()

			