class HashFunction:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    def hash_func_1(self, str_list):
        for j in str_list:
            index = int(j)
            self.the_list[index] = j

    def hash_func_2(self, str_list):
        for k in str_list:
            str_int = int(k)
            index = str_int % 29
            print(f"Mod Index: {index} Value: {str_int}")

            # search for a collision
            while self.the_list[index] != "-1":
                index += 1
                print(f"Collision. Try {index} instead.")
                index %= self.list_size

            self.the_list[index] = k

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        # 6k +/- 1
        j = 5
        while j * j <= num:
            if num % j == 0 or num % (j+2) == 0:
                 return False
            j = j+6
        return True

    def get_next_prime(self, min_size):
        while True:
            if self.is_prime(min_size):
                return min_size
            else:
                min_size += 1

    def increase_list_size(self, min_size):
        new_list_size = self.get_next_prime(min_size)
        self.move_old_list(new_list_size)

    def fill_list_with_none(self):
        for k in range(self.list_size):
            self.the_list.append(None)

    def remove_empty_spaces_in_list(self):
        temp_list = []
        for j in self.the_list:
            if j is not None:
                temp_list.append(j)
        return temp_list

    def move_old_list(self, new_list_size):
        self.list_size = new_list_size
        clean_list = self.remove_empty_spaces_in_list()
        self.fill_list_with_none()
        self.hash_func_2(clean_list)

    def find_key(self, key):
        list_index_hash = int(key) % 29
        while self.the_list[list_index_hash] != "-1":
            if self.the_list[list_index_hash] == key:
                print(f"{key} in index {list_index_hash}")
                return self.the_list[list_index_hash]
            list_index_hash += 1
            list_index_hash %= self.list_size
        return False


if __name__ == "__main__":
    hash_table = HashFunction(30)
    str_list = ["1", "5", "13", "21", "27"]
    hash_table.hash_func_1(str_list)
    # for i in range(hash_table.list_size):
    #     print(i, end=" ")
    #     print(hash_table.the_list[i])

    hash_table_2 = HashFunction(30)
    str_list_2 = [
        "100", "510", "170", "214", "268", "398", "235", "802", "900",
        "723", "699", "1", "16", "999", "890", "725", "998", "990", "989",
        "984", "320", "321", "400", "415", "450", "50", "660", "624"
    ]
    print(f"list size: {len(str_list_2)}")
    hash_func = HashFunction(31)
    hash_table_2.hash_func_2(str_list_2)
    for i in range(hash_func.list_size):
        print(i, end=" ")
        print(hash_func.the_list[i])
    # hash_table_2.find_key("660")

    # print("Find Primes")
    # hash_func.hash_func_2(str_list_2)
    # for i in range(500):
    #     if hash_func.is_prime(i):
    #         print(i)

    hash_func.increase_list_size(60)
    for i in range(hash_func.list_size):
        print(i, end=" ")
        print(hash_func.the_list[i])
