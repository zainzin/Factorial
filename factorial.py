__author__ = 'Zain'

def factorial(number):
    if number < 2:
        return 1
    return number * factorial(number - 1)

print(factorial(5))
