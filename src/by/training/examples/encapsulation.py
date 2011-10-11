# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module includes simple implementation of encapsulation.

'''

class PrivateAccessException(Exception):pass

class PrivateBase:
    
    def __setattr__(self, attrName, attrValue):
        if attrName in self.private:
            raise PrivateAccessException
        self.__dict__[attrName] = attrValue

class AccessorBase:
    
    def __getattr__(self, attrName):
        if not attrName in self.__dict__.keys():
            return 0

class Test(PrivateBase, AccessorBase):
    
    def __init__(self):
        self.__dict__['creditCard'] = 9999
        self.__dict__['private'] = ['creditCard']

if __name__ == '__main__':
    
    instance = Test()
    
    print('Direct access to declared variable - ' + str(instance.creditCard))
    print('Direct access to not existing variable - ' + str(instance.age))
    try:
        print('Trying to set private variable')
        instance.creditCard = 7777
    except PrivateAccessException: 
        print('Access to private attribute is denied!')

