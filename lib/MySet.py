class MySet:
    def __init__(self, elements=None):
        # Initializes the MySet with a list of elements, ensuring no duplicates
        self.dictionary = {}
        if elements:
            for element in elements:
                self.dictionary[element] = True

    def add(self, element):
        # Adds an element to the set
        self.dictionary[element] = True

    def delete(self, element):
        # Deletes an element from the set if it exists
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        # Checks if an element is in the set
        return element in self.dictionary

    def size(self):
        # Returns the size of the set
        return len(self.dictionary)

    # Bonus methods (if needed)
    def clear(self):
        # Clears the set
        self.dictionary.clear()

    def __str__(self):
        # Returns the string representation of the set
        return 'MySet: {' + ','.join(map(str, self.dictionary.keys())) + '}'
