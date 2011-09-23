#!/usr/bin/python

import os
import sys
import subprocess

def probe():
    lastboot = subprocess.check_output(['who', '-b'])
    parts = lastboot.strip().split(None,2)
    
    return [(parts[-1],)]

if __name__ == '__main__':
    for result in probe():
        print 'lastboot', ' '.join(result)

