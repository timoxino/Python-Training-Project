# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module includes simple example of context manager.
'''

class Tracer:
    
    def trace(self, msg):
    
        print('executing of', msg)
    
    def __enter__(self):
    
        print('"with" block is started')
        return self
    
    def __exit__(self, exc_type, exc_value, exc_info):
    
        if exc_type is None:
        
            print('exited normally')
        
        else:
        
            print('raise an exception ', exc_type)
            return False #propogate an exception

if __name__ == '__main__':

    with Tracer() as tr1:
    
        tr1.trace('call of method without exception')
        print('reached')
    
    with Tracer() as tr2:
    
        tr2.trace('call of method and raise exception')
        raise TypeError
        print('not reached')
