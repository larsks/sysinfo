#!/usr/bin/python

import os
import sys

ignored_types = [
    'cgroup',
    'hugetlbfs',
    'mqueue',
    'fusectl',
    'sunrpc',
    'devpts',
    'proc',
    'sysfs',
    'autofs',
    'selinuxfs',
    ]

def probe():
    results = []

    for entry in open('/proc/mounts'):
        fsdev, fsmount, fstype, fsflags, fsfreq, fspassno = \
                entry.strip().split()

        if fstype in ignored_types:
            continue

        vfs = os.statvfs(fsmount)
        size = (vfs.f_blocks * vfs.f_frsize)/1024
        results.append((fsdev, fsmount, fstype, fsflags, str(size)))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'filesystem', ' '.join(result)

