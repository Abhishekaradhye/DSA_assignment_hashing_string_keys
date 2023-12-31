class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            self.table[hash_value].append(string)
        else:
            self.table[hash_value] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            if string in self.table[hash_value]:
                return hash_value
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calculate a
        hash value from a string."""
        return (ord(string[0]) * 100) + ord(string[1])


hash_table = HashTable()

# Test calculate_hash_value

print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case

print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')

print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')

print(hash_table.lookup('UDACIOUS'))
