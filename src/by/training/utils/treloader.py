# Author: Tsimafei Shchytkavets <timoxino@gmail.com>
'''
This module provides functionality for transitive reloading modules.

This exports:

    Functions: 
    
    treload -- uses module or list of modules as parameter. Reloads module and all its dependencies(referring modules).
'''

import types

def treload(*modules):
    reloaded = {}
    for module in modules:
        if type(module) == types.ModuleType:
            if not reloaded.has_key(module):
                _transitive_reload(module, reloaded)                
            
def _transitive_reload(module, reloaded):
        reload(module)
        reloaded[module] = None
        print('Module ' + module.__name__ + ' was reloaded.')
        for attrValue in module.__dict__.values():
            if type(attrValue) == types.ModuleType:
                if not reloaded.has_key(attrValue):
                    _transitive_reload(attrValue, reloaded)