

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        # cheating a little bit here by using a python list; however, won't use any built in array functions
        self.elements = [None] * capacity
        self.count = 0

print(bin(17 << 2))


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
    return hash % max


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    hash_key = hash(key, hash_table.capacity)
    if hash_table.elements[hash_key]:
        print('Warning! Overwriting existing value')
    hash_table.elements[hash_key] = value
    print(hash_table.elements)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    hash_key = hash(key, hash_table.capacity)
    if hash_table.elements[hash_key] == None:
        print('Nothing here')
        return
    hash_table.elements[hash_key] = None
    print(hash_table.elements)


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
