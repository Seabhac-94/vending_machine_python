"""
x = 2
y = 1

assert x < y, "{0} should be less than {1}".format(x, y)

print(x + y)
"""

"""
def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("A") == 1, "One Uppercase"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("#¢§€#") == 0, "Special characters"
assert count_upper_case("HeLLo ZAc") == 5, "Custom sentence"



print("all test passed")
"""
#challenge TEST AFTER
"""
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty String"
assert count_upper_case("aBcDeFG") == 4, "Alphabet"
assert count_upper_case("this is a test") == 0, "this is a test"
assert count_upper_case("12¢§09") == 0, "Special characters"
assert count_upper_case("ALL CAPLOCKS") ==11, "Meant to fail"


print("Tests Passed")
"""

"""

def is_even(number):
    return number % 2 == 0

def even_number_of_evens(numbers):
    
    evens = 0
    for number in numbers:
        if is_even(n):
            evens += 1

    if evens == 0:
        return False
    else:
        return is_even(evens)
    

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"


print ("All tests passed")

"""

