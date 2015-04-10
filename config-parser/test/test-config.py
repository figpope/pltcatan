#!/usr/bin/env python
import sys
sys.path.append('..')
from settings import Settings

def prettyPrint(structure, indent = 0):
    for key, value in structure.iteritems():
        sys.stdout.write('    ' * indent + key + ': ')
        if isinstance(value, dict):
            sys.stdout.write('\n')
            prettyPrint(value, indent + 1)
        else:
            sys.stdout.write(str(value) + '\n')

if __name__ == '__main__':
    settings = Settings('../default.skit')
