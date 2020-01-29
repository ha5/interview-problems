# Section 1: cache implementation

class LRUCache:
    """Least Recently Used Cache class implementation"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # initialize an empty cache using dictionary data structure
        self.cache = {}

    def get(self, key: int) -> int:
        """
        Return the associated value of a given key.
        Return -1 if key not found.
        """
        if key in self.cache:
            # remove key from cache
            val = self.cache.pop(key)
            # reinsert key back so that it's at the front of the cache
            self.cache[key] = val
            print("The value of key {0} is {1}".format(str(key), str(val)))
            return val
        print("Sorry. Item doesn't exist in cache...")
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Put a new pair of key-value to the front of the cache
        """
        # if exist, pop it, and reinsert key at the front of cache
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        # else if (limit is not reached), insert key
        elif self.capacity > len(self.cache):
            self.cache[key] = value
        # else if cache limit is reached, evict the Least Recently Used item
        # before putting
        elif self.capacity == len(self.cache):
            eviction_item = list(self.cache.keys())[0]
            self.cache.pop(eviction_item)
            self.cache[key] = value

    def delete(self, key):
        """
        Delete a key if exists
        """
        if key in self.cache:
            self.cache.pop(key)
            print("Item {} has been removed from cache.".format(str(key)))
        else:
            print("Sorry. Item doesn't exist in cache...")

    def reset(self):
        """
        Set the cache dictionary to empty
        """
        self.cache = {}
        print("All items in your cache have been EEEEVICTED.")


# Section 2: user interface and object initialization

capacity = int(input("Please enter cache capacit y (for example: 4): "))
print("Acknowledged. Your cache capacity is " + str(capacity))

MY_CACHE = LRUCache(capacity)

while True:
    print("Your current cache items: ")
    print(MY_CACHE.cache)
    ACTION = input("Please enter desired cache action " +
                   "(any of the following: get, put, delete, reset): ")
    if ACTION == "reset":
        MY_CACHE.reset()

    elif ACTION == "get":
        key = int(input("Please enter a key to GET from cache: "))
        MY_CACHE.get(key)

    elif ACTION == "put":
        key = int(input("Please enter a key to PUT to cache: "))
        value = int(input("Please enter a value for the above key: "))
        MY_CACHE.put(key, value)

    elif ACTION == "delete":
        key = int(input("Please enter a key to DELETE from cache: "))
        MY_CACHE.delete(key)

    else:
        print("Action not supported. Please try again.")
