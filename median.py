"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
if len(numbers) % 2 == 0:
    first_index = len(numbers) / 2 - 1
    second_index = len(numbers) / 2
    median = (numbers[int(first_index)] + numbers[int(second_index)])/2
    print(median)
else:
    index = (len(numbers) - 1) / 2
    print(numbers[int(index)])
