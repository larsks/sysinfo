#!/usr/bin/python

import os
import sys

grp_fields = [
        'cn',
        'groupPassword',
        'gidNumber',
        'members'
        ]


def probe():
    results = []
    groups = {}

    for line in open('/etc/group'):
        g = dict(zip(grp_fields, line.strip().split(':')))
        groups[g['cn']] = g

    for cn in sorted(groups):
        results.append((cn, groups[cn]['gidNumber']))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'group', ' '.join(result)


