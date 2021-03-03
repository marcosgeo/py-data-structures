import timeit


def get_sum(max_num):
    sol = 0
    for i in range(1, max_num + 1):
        sol += i
    return sol


def get_sum_2(max_num):
    sol = 0
    i = 1
    while i < max_num:
        sol += i
        i += 1
    return sol


def get_sum_3(max_number):
    return max_number * (max_number + 1)/2

print("Testing get_sum")
print(timeit.repeat(stmt='get_sum(100000)', repeat=5, number=1, globals=globals()))

print("Testing get_sum_2")
print(timeit.repeat(stmt="get_sum_2(100000)", repeat=5, number=1, globals=globals()))

print("Testing get_sum_3")
print(timeit.repeat(stmt="get_sum_3(100000)", repeat=5, number=1, globals=globals()))
