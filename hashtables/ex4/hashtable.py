class HashTableEntry:

    def __init__(self, key, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

    def set_next(self, new_next):
        self.next = new_next

    def set_value(self, value):
        self.value = value


class HashTable:

    def __init__(self, capacity=6):
        self.capacity = capacity
        self.buckets = [LinkedList() for i in range(capacity)]

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        current_bucket = 0
        total = 0

        while current_bucket <= self.capacity - 1:
            total = total + self.buckets[current_bucket].count
            current_bucket += 1

        return total / self.capacity

    def resize_test(self):
        if self.get_load_factor() > 0.7:

            print("load larger than 0.7, doubling capacity")
            self.resize(self.capacity * 2)
        elif self.get_load_factor() < 0.2:
            print("load smaller than 0.2, halving capacity")
            self.resize(self.capacity // 2)
        else:
            print(f"Current load factor {float(self.get_load_factor())}")

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        bucket = self.buckets[self.hash_index(key)]

        bucket.add_to_list(key, value)
        # print(self.get_load_factor())
        # self.resize_test()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        bucket = self.buckets[self.hash_index(key)]
        bucket.deleteEntry(key)
        # print(self.get_load_factor())
        # self.resize_test()

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here

        # for k, v in self.buckets[self.hash_index(key)]:
        #     if k == key:
        #         return v
        # return None
        value = self.buckets[self.hash_index(key)].contains(key)
        return value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """

        # Your code here
        # save old data
        old_buckets = self.buckets
        old_capacity = self.capacity
        curr_bucket = 0

        # set new capacity for re-entry
        self.capacity = new_capacity
        self.buckets = [LinkedList() for i in range(new_capacity)]

        # feed old data into new buckets
        while curr_bucket <= old_capacity - 1:
            resize_count = 0
            tempEntry = old_buckets[curr_bucket].head
            while resize_count <= old_buckets[curr_bucket].count - 1:
                bucket = self.buckets[self.hash_index(tempEntry.key)]
                bucket.add_to_list(tempEntry.key, tempEntry.value)
                tempEntry = tempEntry.next
                resize_count += 1
            curr_bucket += 1


class LinkedList:

    def __init__(self, count=0):
        self.head = None
        self.count = count

    def add_to_list(self, key, value):
        # if empty add to head
        hashEntry = HashTableEntry(key, value)
        if self.head is None:
            self.count += 1
            self.head = hashEntry

        # if key present, update
        if self.contains(key) is not None:
            self.update(key, value)

        # else, add to head
        else:
            self.add_to_head(key, value)
            self.count += 1

    def update(self, key, value):
        current = self.head
        found = False
        while current is not None:
            if current.key == key:
                current.set_value(value)
                break

            current = current.next

        return found

    def add_to_head(self, key, value):
        hashEntry = HashTableEntry(key, value)
        # bucket NOT empty
        if self.head is not None:
            hashEntry.set_next(self.head)
        # bucket empty
        self.head = hashEntry
        self.count += 1

    def contains(self, key):
        current = self.head
        found = None
        while current is not None:
            if current.key == key:
                found = current.value
                break

            current = current.next

        return found

    def deleteEntry(self, key):
        tempEntry = self.head
        if self.head.key == key:
            self.head = self.head.next
            self.count -= 1
            return ("head deleted")

        else:
            tempEntry = self.head

            while tempEntry.next is not None:
                if tempEntry.next.key == key:
                    tempEntry.next = tempEntry.next.next
                    self.count -= 1
                    return("deleted")
                tempEntry = tempEntry.next
            return("Key not found")
