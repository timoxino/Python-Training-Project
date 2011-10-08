# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module includes iterated class definition. Class provides functionality for iteration based on iterator and indexing.
Class and module include two implementations of function-generator.
There is a simple self-test for all of this iteration protocol implementations.

'''

class iterentity:
    
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __getitem__(self, index):
        if self.stop - self.start < index + 1:
            raise StopIteration
        return self.start + 1 + index
    
    def next(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self.start
    
    def generate(self):
        self.start += 1
        for current in range(self.start, self.stop + 1):
            yield current

def generate(start, stop):
    for current in range(start, stop + 1):
        yield current

if __name__ == '__main__':
    
    for value in generate(1, 5):
        print(value)
    
    instance = iterentity(6, 10)
    for value in instance:
        print(value)
    
    for value in iterentity(11, 15).generate():
        print(value)
    
    print(iterentity(16, 20)[0])

