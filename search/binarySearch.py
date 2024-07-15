# Algorithm: Binary Search
# Type: Searching Algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1)

# 1. Create a list of numbers
# 2. Create a function called binary_search
# 3. Create a variable called low and set it to 0
# 4. Create a variable called high and set it to the length of numbers minus 1
# 5. While low is less than or equal to high:
# 6. Create a variable called mid and set it to the average of low and high
# 7. If the number at index mid is equal to the target:
# 8. Return mid
# 9. If the number at index mid is greater than the target:
# 10. Set high to mid minus 1
# 11. Otherwise:
# 12. Set low to mid plus 1
# 13. Return None


numbers = [0, 1, 3, 4, 5, 6, 17, 18, 19, 20, 21, 22, 23, 34, 35, 36, 37, 38, 39, 40, 51, 52, 53, 54, 55, 56,
           57, 58, 67, 68, 69, 70, 71, 72, 73, 74, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95,  100]


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


print("Element Index is: ", binary_search(numbers, 5))
