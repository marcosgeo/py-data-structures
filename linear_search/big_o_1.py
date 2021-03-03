#Big O notation: O(N)
import time
import random


list_1 = []
start_time = 0
end_time = 0


def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1, 99))
    return new_list


list_1 = generate_rand_list(10)
def add_item_to_list(num):
    list_.append(num)


def linear_search(val):
    val_found = "Value not found"
    for i in list_1:
        if i == val:
            val_found = "Value found"
    print(val_found)


print("Testing linear search")
list_1 = generate_rand_list(10)
start_time = time.time()
linear_search(10000)
print(f"{time.time() - start_time} seconds")


print("Testing linear search")
list_1 = generate_rand_list(1000)
start_time = time.time()
linear_search(10000)
print(f"{time.time() - start_time} seconds")


print("Testing linear search")
list_1 = generate_rand_list(100000)
start_time = time.time()
linear_search(10000)
print(f"{time.time() - start_time} seconds")