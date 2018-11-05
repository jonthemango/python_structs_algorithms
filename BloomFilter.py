
'''
BloomFilter is a data structure with two public methods: insert O(1) and maybeContains O(1). (Assuming hash functions are O(1))
Memory is also O(1). 
https://en.wikipedia.org/wiki/Bloom_filter
The purpose of the data structure is to check if elements have maybe previously passed into the filter.
When querying the BloomFilter returns True if the value may have passed through and False if it certainly never passed through.
The element itself never needs to be stored within the data structure.
'''
class BloomFilter:

    struct = []

    def __init__(self, size=100):
        self.size = size # size of the default array
        self._set_up_struct() # set all bits to False in the struct

    def _set_up_struct(self):
        for i in range(self.size):
            self.struct.append(False)

    def _hash1(self, element):
        hv = hash(element) # hash the element 
        return hv % self.size # and convert it an int between 0 and size

    def _hash2(self, element):
        hv = hash(str(hash(element))) # hash the str of the element's hash 
        return hv % self.size # and convert it an int between 0 and size
    
    def _hash3(self, element):
        hv = hash(str(hash(str(hash(element))))) # hash the str of the hash of the str of the element's hash 
        return hv % self.size # and convert it an int between 0 and size

    '''
    insert(element): 
        - hash the element k times (in this case 3) to values between 0 and the size of the array. 
        - At those indices set the values to True
    '''
    def insert(self, element):
        hv1 = self._hash1(element) # get the first hash value 
        hv2 = self._hash2(element) # get the second hash value 
        hv3 = self._hash3(element) # get the third hash value 

        # set the position at the hashvalue to true 
        self.struct[hv1] = True 
        self.struct[hv2] = True
        self.struct[hv3] = True

    '''
    maybeContains(element): 
        - hash the element k times (in this case 3) to values between 0 and the size of the array. 
        - At those indices check if the values are all True
        - True => MAYBE the element has been inserted before
        - False => Definitely never passed through
    '''
    def maybeContains(self, element):
        hv1 = self._hash1(element) # get the first hash value 
        hv2 = self._hash2(element) # get the second hash value 
        hv3 = self._hash3(element) # get the third hash value 

        # if all are true  => then MAYBE the element has been inserted before 
        # if any one of them is false => then the element NEVER passed through before
        return self.struct[hv1] and self.struct[hv2] and self.struct[hv3]

    def __repr__(self):
        return '[' +  ', '.join(str(e) for e in self.struct) + ']'



bloom = BloomFilter(size=5) # set size to 5 to demonstrate possible false-positives

bloom.insert('Bloom Insert') # Insert element
print("BloomFilter after first insert: " + str(bloom))

bloom.insert('Bloom 2') # Insert element
print("BloomFilter after second insert: " + str(bloom))

bloom.insert('Bloom 3') # Insert element
print("BloomFilter after third insert: " + str(bloom))

print("Maybe Contains: 'Bloom Insert': " + str(bloom.maybeContains('Bloom Insert'))) # returns true
print("Maybe Contains: 'Bloom 2': " + str(bloom.maybeContains('Bloom 2'))) # returns true
print("Maybe Contains: 'Bloom 3': " + str(bloom.maybeContains('Bloom 3'))) # returns true
print("Maybe Contains: 'Never was in....': " + str(bloom.maybeContains('Never was in....'))) # returns false
print("Maybe Contains: 'Still returns True.': " + str(bloom.maybeContains('Still returns True.'))) # never inserted but still returns true









        
