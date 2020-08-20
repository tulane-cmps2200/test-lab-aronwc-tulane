def sum_of_squares(a):
	return sum([v**2 for v in a])

def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([]) == 0