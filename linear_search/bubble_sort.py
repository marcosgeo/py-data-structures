# O(N^2)
import time
import random

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list


def bubble_sort(list_1):
    list_size = len(list_1)
    for i in range(list_size):
        for j in range(0, list_size -i -1):
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]
            # for k in list_1:
            #     print(k, end=", ")
            # print()


list_1 = generate_rand_list(100)
start_time = time.time()
bubble_sort(list_1)
print(f"{time.time() - start_time} seconds")

list_2 = generate_rand_list(1000)
start_time = time.time()
bubble_sort(list_2)
print(f"{time.time() - start_time} seconds")

list_3 = generate_rand_list(10000)
start_time = time.time()
bubble_sort(list_3)
print(f"{time.time() - start_time} seconds")