# Algorithm: Quicksort
# Type: Sorting Algorithm
# Time Complexity: O(n log n)
# Space Complexity: O(n)

# 1. Create a list of numbers
# 2. If the list is empty has 1 or fewer elements, return the list
# 3. Otherwise:
# 4. Select the pivot element from the list
# 5. Create a list of elements less than or equal to the pivot
# 6. Create a list of elements greater than the pivot
# 7. Return the concatenation of:
# 8. The result of quicksort on the list of elements less than or equal to the pivot
# 9. The pivot element
# 10. The result of quicksort on the list of elements greater than the pivot


numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[0]
        smallers = [i for i in numbers[1:] if i <= pivot]
        greaters = [i for i in numbers[1:] if i > pivot]
        return quicksort(smallers) + [pivot] + quicksort(greaters)


print(quicksort(numbers))
