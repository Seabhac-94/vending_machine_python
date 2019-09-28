def number_of_evens(numbers):
    return 0

def odd_number(a):
    return a

my_collection = {1, 2, 3, 4, 5}


def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} contains {1}".format(collection, item)

def test_between(lower, value, upper):
    assert value < upper and value > lower, "{1} is not between {0} or {2}".format(lower, value, upper)



#tests

#test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)
#test_not_equal(odd_number(5), odd_number(5))
#test_is_in(my_collection, 6)
#test_not_in(my_collection, 3)
#test_between(1, 11, 10)

