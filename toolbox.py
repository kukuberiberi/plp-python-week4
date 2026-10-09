# Function 1 - double
def double(number):
    return number * 2


# Function 2 - is_pass
def is_pass(score):
    return score >= 50


# Function 3 - greet
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# Test lines
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Kuku"))
print(greet("Beriberi", "Habari"))