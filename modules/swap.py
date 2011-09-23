#!/usr/bin/python

import os
import sys

swap_fields = [
        'device',
        'type',
        'size',
        'used',
        'priority',
        ]

def probe():
    results = []

    for line in sorted(open('/proc/swaps')):
        if not line.strip() or line.startswith('Filename'):
            continue

        data = dict(zip(swap_fields, line.strip().split()))
        results.append((data['device'], data['type'],
            data['size']))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'swap', ' '.join(result)

