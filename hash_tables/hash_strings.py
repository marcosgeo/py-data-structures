class HashFunction:
    def __init__(self, size):
        self.list_size = size
        self.the_list = []
        for i in range(size):
            self.the_list.append("-1")

    def hash_string(self, str_to_hash):
        hash_val = 0
        hash_sum = 0
        for i in range(len(str_to_hash)):
            char_code = ord(str_to_hash[i]) - 96
            hkv_temp = hash_val
            hash_sum += (hash_val *27 + char_code)
        return hash_sum

    def hash_str_list(self, str_list):
        for str_to_hash in str_list:
            hash_sum = self.hash_string(str_to_hash)
            step_distance = 7 - (hash_sum % 7)
            while self.the_list[hash_sum] != "-1":
                hash_sum += step_distance
                hash_sum %= self.list_size
            self.the_list[hash_sum] = str_to_hash

    def find(self, value):
        value_index = self.hash_string(value)
        step_distance = 7 - (value_index % 7)
        while self.the_list[value_index] != "-1":
            if self.the_list[value_index] == value:
                print(f"{value} in index {value_index}")
                return self.the_list[value_index]
            value_index += step_distance
            value_index %= self.list_size
        return false

if __name__ == "__main__":
    words_to_add = [
        "ace", "act", "add", "age", "ago", "aid", "aim",
        "air", "all", "amp", "and", "ant", "any", "ape",
        "apt", "arc", "are", "ark", "arm", "art", "ash",
        "ask", "asp", "ate", "atm", "awe", "axe", "aye"
    ]

    hash_func = HashFunction(61)
    hash_func.hash_str_list(words_to_add)
    hash_func.find("ask")