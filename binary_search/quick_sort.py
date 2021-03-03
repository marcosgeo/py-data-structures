import random
import time


start_time = 0
end_time = 0

def partition(list_1, start, end):
    pivot = list_1[start]
    low = start + 1
    high = end
    while True:
        while low <= high and list_1[high] >= pivot:
            high = high -1
        while low <= high and list_1[low] <= pivot:
            low = low + 1

        if low <= high:
            list_1[low], list_1[high] = list_1[high], list_1[low]
        else:
            break
    list_1[start], list_1[high] = list_1[high], list_1[start]
    return list_1, high


def quick_sort(list_1, start, end):
    # Demonstrates how the Quick sort works
    for k in list_1:
        print(k, end=", ")
    print()

    if start >= end:
        return
    new_list, part = partition(list_1, start, end)
    quick_sort(new_list, start, part - 1)
    quick_sort(new_list, part + 1, end)


def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list

# O(log N)
 
def binary_search(list_1: list, value: int):
    list_size = len(list_1)
    low_index = 0
    high_index = list_size -1
    while low_index <= high_index:
        mid_index = int((high_index + low_index) / 2)
        if list_1[mid_index] < value:
            low_index = mid_index + 1
        elif list_1[mid_index] > value:
            high_index = mid_index - 1
        else:
            print(f"Found a match for {value} at index {mid_index}")
            low_index = high_index + 1


list_1 = [5, 9, 10, 2, 8, 1, 7, 3, 11]
quick_sort(list_1, 0, len(list_1))
print(list_1)
binary_search(list_1, 7)