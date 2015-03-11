'''
GotoNewest

A tool to quickly transfer to the latest directory
created in a base directory, provided the name of
the base directory is supplied as an argument
'''

import os
import sys
import gn_helper

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
    latest_subdir = get_latest_modified_subdir(basepath)
    return latest_subdir

def get_latest_modified_subdir(basepath):
    ''' Iterate through all the subdirectories in a given path
    and return the one with the latest modified time
    '''
    # TODO: There has to be a better way of doing this
    all_subdirs = os.listdir(basepath)
    latest = os.path.getmtime(basepath + '/' + all_subdirs[0])
    latest_subdir = all_subdirs[0]
    for subdir in all_subdirs:
        mtime = os.path.getmtime(basepath + '/' + subdir)
        if mtime > latest:
            latest = mtime
            latest_subdir = subdir

    return latest_subdir

def main():
    ''' Get the latest directory created in the directory
    set as basepath in the config file, and then cd into it
    '''
    basepath = gn_helper.get_basepath()
    if basepath is not None:
        os.chdir(basepath)
        print 'Testing: in', os.getcwd()
    else:
        print 'Sorry, the basepath is not valid'

if __name__ == '__main__':
    main()
