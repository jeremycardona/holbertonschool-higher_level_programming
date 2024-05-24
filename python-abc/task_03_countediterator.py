#!/usr/bin/python3
"""Module for CountedIterator class"""
class CountedIterator:
    """CountedIterator methods"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        self.counter += 1
        return next(self.iterator)
    
    def get_count(self):
        return self.counter