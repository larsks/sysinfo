#!/usr/bin/python

import os
import sys

pwd_fields = [
        'uid',
        'userPassword',
        'uidNumber',
        'gidNumber',
        'description',
        'homeDirectory',
        'loginShell'
        ]

def probe():
    results=[]
    users = {}

    for line in open('/etc/passwd'):
        p = dict(zip(pwd_fields, line.strip().split(':')))
        users[p['uid']] = p

    for uid in sorted(users):
        results.append((uid, users[uid]['uidNumber'],
            users[uid]['gidNumber'], users[uid]['homeDirectory']))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'user', ' '.join(result)


