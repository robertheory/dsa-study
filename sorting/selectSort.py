# Algorithm: Selection Sort
# Type: Sorting Algorithm
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# 1. Create a list of numbers
# 2. Create an empty list called sorted_numbers
# 3. While numbers is not empty:
# 4. Find the minimum number in numbers
# 5. Add the minimum number to sorted_numbers
# 6. Remove the minimum number from numbers
# 7. Print sorted_numbers

# import json
# file = open('./inputs/sortingInput.json')
# numbers = json.load(file)

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

sorted_numbers = []

while numbers:
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    sorted_numbers.append(minimum)
    numbers.remove(minimum)

print(sorted_numbers)
