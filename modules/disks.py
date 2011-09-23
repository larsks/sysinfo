#!/usr/bin/python

import os
import sys

from sysinfo.sysdir import SysDir

def probe():
    results = []
    disks = os.listdir('/sys/class/block')

    for devname in sorted(disks):
        dev = SysDir(os.path.join('/sys/class/block', devname))
        results.append((devname, dev['size']))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'disk', ' '.join(result)

