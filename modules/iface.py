#!/usr/bin/python

import os
import sys

import socket

from sysinfo.sysdir import SysDir
from sysinfo.getifaddrs import getifaddrs

AF_MAP = [
        ('inet', socket.AF_INET),
        ('inet6', socket.AF_INET6)
        ]

def probe():
    results = []

    interfaces = os.listdir('/sys/class/net')
    addresses = getifaddrs()

    for ifname in sorted(interfaces):
        ifdev = SysDir(os.path.join('/sys/class/net', ifname))

        results.append((ifname, 'index', ifdev['ifindex'], 
            'type', ifdev['type'],
            'hw', ifdev['address']))

        for afname, af in AF_MAP:
            try:
                for addr in addresses[ifname][af]:
                    data = [ifname, afname, addr['addr']]
                    if 'netmask' in addr:
                        data.extend(['netmask', addr['netmask']])
                    results.append(tuple(data))
            except KeyError:
                continue

    return results

if __name__ == '__main__':
    for result in probe():
        print 'iface', ' '.join(result)


