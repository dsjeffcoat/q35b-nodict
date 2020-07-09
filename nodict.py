#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Diarte Jeffcoat w/help from Kyle Negley and Randy Charity Jr'


class Node:
    def __init__(self, key, value=None):
        '''Set up the instances for the class object'''
        self.hash = hash(key)
        self.key = key
        self.value = value

    def __repr__(self):
        '''Print a human-readable representation
        of its key/value contents when asked'''
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        '''Object should be able to compare itself to other Node objects'''
        return self.key == other.key

    def __hash__(self):
        '''Provide an instance for the hash value of the object'''
        return self.hash


class NoDict:
    def __init__(self, num_buckets=10):
        '''Sets class initializer to create
        the buckets according to a size parameter'''
        self.buckets = [[] for i in range(num_buckets)]
        self.num_buckets = num_buckets

    def __repr__(self):
        """Return string representation of the contents of the buckets."""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value):
        '''Should accept a new key and value, and
         store it into the NoDict object. However, this method
          should not allow duplicate keys.'''
        new_node = Node(key, value)
        index = hash(new_node) % self.num_buckets
        if new_node in self.buckets[index]:
            existing_node = self.buckets[index].index(new_node)
            self.buckets[index][existing_node] = new_node
        self.buckets[index].append(new_node)

    def get(self, key):
        '''Method should perform a key-lookup in the NoDict class. It should
        accept just one parameter: The key to look up. If the key is found
         in the NoDict class, return its associated value.
         If the key is not found, raise a KeyError exception.'''
        node_to_find = Node(key)
        index = hash(node_to_find) % self.num_buckets

        if node_to_find not in self.buckets[index]:
            raise KeyError(f'{key} not found')
        return self.buckets[index][0].value

    def __getitem__(self, key):
        '''Implement this magic "dunder" method within the NoDict
        class to enable square-bracket reading behavior. This will
        make the class behave more like a regular dictionary.'''
        return self.get(key)

    def __setitem__(self, key, value):
        '''Implement this magic "dunder" method within the NoDict
        class to enable square-bracket assignment behavior. This
        will make the class behave more like a regular dictionary.'''
        self.add(key, value)
