"""
Tobenna Nwufo
CIS 2348
2054054
"""

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        largest_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[largest_index]:
                largest_index = j
        numbers[i], numbers[largest_index] = numbers[largest_index], numbers[i]
        print(*numbers, end=" ")
        print()
    return numbers


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    selection_sort_descend_trace(numbers)

