
def get_index(data_list, a_string):
    # Variable to store the result(updated after each iteration)
    result = 0
    for a_character in a_string:
        # convert the character to a number (using ord)
        a_number = ord(a_character)
        # update result by adding the numbers
        result += a_number

    list_index = result % len(data_list)
    return list_index


MAX_HASH_TABLE_SIZE = 4096


# class BasicHashTable:
#     def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
#         # Create a list of size max_size with all values None
#         self.data_list = [None] * max_size
#
#     def insert(self, key, value):
#         # find the index for the key using get_index
#         idx = get_index(self.data_list, key)
#
#         # #2 store the key-value pair at the right index
#         self.data_list[idx] = (key, value)
#
#     def find(self, key):
#         # Find the index for the key using get_index
#         idx = get_index(self.data_list, key)
#
#         # Retrieve the data stored at the index
#         kv = self.data_list[idx]
#
#         # return the value if found, else return none
#         if kv is None:
#             return None
#         else:
#             key, value = kv
#             return value
#
#     def update(self, key, value):
#         # Find the index for the key using get_index
#         idx = get_index(self.data_list, key)
#
#         # Store the new key-value pair at the right index
#         self.data_list[idx] = (key, value)
#
#     def list_all(self):
#         # Extract the key from each key value pair
#         return [kv[0] for kv in self.data_list if kv is not None]
#
#
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)

    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]

        # If it is none, return the index
        if kv is None:
            return idx

        # If the stored key matches the given key, return the index
        k, v = kv
        if key == k:
            return idx

        # move to the next index
        idx += 1

        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0
#
#
# class ProbingHashTable:
#     def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
#         # create a list of size max_size with all values None
#         self.data_list = [None] * max_size
#
#     def insert(self, key, value):
#         # 1. Find the index for the key using get_valid_index
#         idx = get_valid_index(self.data_list, key)
#
#         # 2. Store the key-value pair at the right index
#         self.data_list[idx] = (key, value)
#
#     def find(self, key):
#         # 1. Find the index for the key using get_valid_index
#         idx = get_valid_index(self.data_list, key)
#
#         # 2. Retrieve the data stored at the index
#         kv = self.data_list[idx]
#
#         # 3. Return the value if found, else return None
#         return None if kv is None else kv[1]
#
#     def update(self, key, value):
#         # 1. Find the index for the key using the get_valid_index
#         idx = get_valid_index(self.data_list, key)
#
#         # 2. Store the new key-value pair at the right index
#         self.data_list[idx] = (key, value)
#
#     def list_all(self):
#         # 1. Extract the key from each key-value pair
#         return [kv[0] for kv in self.data_list if kv is not None]


# optional (implement a python friendly interface for the hash table)
class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
        self.max_size = max_size

    def get_valid_index(self, key):
        idx = hash(key) % self.max_size

    def __getitem__(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        return None if kv is None else kv[1]

    def __setitem__(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    # def __delete__(self, key):
    #     idx = get_valid_index(self.data_list, key)
    #     self.data_list[idx] = 0, 0

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}". format('.\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)


data_list = [None] * MAX_HASH_TABLE_SIZE

# basic_table = BasicHashTable(max_size=1024)
# basic_table.insert('Aakash', '9999999999')
# basic_table.insert('Hemanth', '8888888888')
# basic_table.update('Aakash', '7777777777')
# basic_table.insert('listen', 99)
# basic_table.insert('silent', 200)
#
# data_list2 = [None] * MAX_HASH_TABLE_SIZE
# data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
#
# probing_table = ProbingHashTable()
# probing_table.insert('listen', 99)
# probing_table.insert('silent', 200)
# probing_table.insert('listen', 101)

table = HashTable()

table['a'] = 1
table['b'] = 34


print(table.__len__())

























