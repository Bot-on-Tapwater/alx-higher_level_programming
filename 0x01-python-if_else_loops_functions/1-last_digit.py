#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
not_number = number
if (not_number < 0):
    not_number *= -1

while (not_number > 10):
    not_number %= 10

if (not_number > 5):
    print(f"Last digit of {number:d} is {not_number:d} and is greater than 5")

elif (not_number == 0):
    print(f"Last digit of {number:d} is {not_number:d} and is 0")

else:
    print(f"Last digit of {number:d} is {not_number:d}", end=' ')
    print(f"and is less than 6 and not 0")
