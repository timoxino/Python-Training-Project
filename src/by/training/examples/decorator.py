# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module includes simple implementation of encapsulation.

'''

class tracer:
    
    def __init__(self, func):
        
        self.func = func
        self.counter = 0
    
    def __call__(self, *args):
        
        self.counter += 1
        print('function \'%s\' has been called %d time(s)' % (self.func.__name__, self.counter))
        
        self.func(*args)

@tracer
def printit(arg1, arg2):
        
    print('Print first arg = \'%s\' and second one = \'%s\'' % (arg1, arg2))



if __name__ == '__main__':
    
    printit('Hello', 'World')
    printit('Goodbye', 'World')
