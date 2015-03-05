'''
GotoNewest

A tool to quickly transfer to the latest directory
created in a base directory, provided the name of
the base directory is supplied as an argument
'''

import os

def transfer(basepath=None):
    ''' Transfer to the newest directory in the basepath
    directory
    '''
    if basepath is None:
        raise AttributeError
    subdirs = os.listdir(basepath)
    if len(subdirs) == 0:
        raise AttributeError
    if len(subdirs) == 1:
        return subdirs.pop()
