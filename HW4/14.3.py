"""
Tobenna Nwufo
CIS 2348
2054054
"""
import math

num_calls = 0

def partition(user_ids, i, k):
    # Select the pivot as the middle element between i and k
    pivot = user_ids[math.floor((i + k) / 2)]
    # Initialize two pointers, left and right, pointing to the start and end of the subarray
    left = i
    right = k
    # Continue swapping elements until the left and right pointers meet or cross each other
    while left <= right:
        # Move the left pointer to the right until it points to an element that is greater than or equal to the pivot
        while user_ids[left] < pivot:
            left += 1
        # Do the same with the right pointer to the left but less than this time
        while user_ids[right] > pivot:
            right -= 1
        # If both pointers have not crossed each other,swap the elements they point to using tuple unpacking
        if left <= right:
            user_ids[left], user_ids[right] = user_ids[right], user_ids[left]
            left += 1
            right -= 1

    # Return the position of the pivot element
    return left


def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    # If the array has more than one element, partition it and quicksort the two resulting subarrays recursively
    if i < k:
        pos = partition(user_ids, i, k)
        quicksort(user_ids, i, pos - 1)
        quicksort(user_ids, pos, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while (user_id != "-1"):
        user_ids.append(user_id)
        user_id = input()

    quicksort(user_ids, 0, len(user_ids) - 1)

    print(num_calls)

    for user_id in user_ids:
        print(user_id)