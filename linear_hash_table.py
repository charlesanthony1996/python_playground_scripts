class LinearHashTable:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]
        self.threshold = 0.7



    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]


        # check for duplicates and update if necessary
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1


        # check if the load factor exceeds the threshold, then split
        if self.size / self.capacity > self.threshold:
            self.split()

        
    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]


        for existing_key, value in bucket:
            if existing_key == key:
                return value

    
        return None


    def split(self):
        new_capacity = self.capacity * 2
        new_buckets = [[] for _ in range(new_capacity)]


        for bucket in self.buckets:
            for key, value in bucket:
                new_index = hash(key) % new_capacity
                new_buckets[new_index].append((key, value))

        
        self.capacity = new_capacity
        self.buckets = buckets


    def __str__(self):
        return str(self.buckets)


# example usage
hash_table = LinearHashTable()
# insert key value pair to the table

hash_table.insert("apple", 1)
hash_table.insert("orange", 2)
hash_table.insert("banana", 4)
hash_table.insert("pineapple", 10)

print(hash_table)

print(hash_table.get("apple"))
print(hash_table.get("orange"))

# updating existing values
hash_table.insert("apple", 7)
print("updated value for apple: ", hash_table.get("apple"))


# demonstrate splitting
hash_table.insert("fig", 4)
print("hash table after splitting")
print(hash_table)