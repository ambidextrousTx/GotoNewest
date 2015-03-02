'''
GotoNewest

A tool to quickly transfer to the latest directory
created in a base directory, provided the name of
the base directory is supplied as an argument
'''

def transfer(basepath=None):
    ''' Transfer to the newest directory in the basepath
    directory
    '''
    if basepath is None:
        raise AttributeError
