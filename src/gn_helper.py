'''
Helper methods for GotoNewest
'''

CONFIG_FILE = '../config/gn.cnf'

def get_basepath():
    ''' Read the basepath as saved in the config
    file and return it (or None if there is a problem)
    '''
    basepath = None
    with open(CONFIG_FILE, 'r') as fhi:
        for line in fhi:
            # Allow for comments
            if line.startswith('#'):
                pass
            else:
                info = line.strip().split('=')
                if info[0] == 'basepath':
                    basepath = info[1]

    return basepath
