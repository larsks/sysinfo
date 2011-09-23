#!/usr/bin/python

import os
import sys

uname_fields = [
        'sysname',
        'nodename',
        'release',
        'version',
        'machine',
        ]

def probe():
    results = []

    uname = dict(zip(uname_fields, os.uname()))
    for k in sorted(uname):
        results.append((k, uname[k]))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'uname', ' '.join(result)
