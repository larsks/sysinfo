#!/usr/bin/python

import os
import sys
import subprocess

keywords=[
    'bios-vendor',
    'bios-version',
    'bios-release-date',
    'system-manufacturer',
    'system-product-name',
    'system-version',
    'system-serial-number',
    'system-uuid',
    'baseboard-manufacturer',
    'baseboard-product-name',
    'baseboard-version',
    'baseboard-serial-number',
    'baseboard-asset-tag',
    'chassis-manufacturer',
    'chassis-type',
    'chassis-version',
    'chassis-serial-number',
    'chassis-asset-tag',
    'processor-family',
    'processor-manufacturer',
    'processor-version',
    'processor-frequency',
    ]

def probe():
    results = []
    for k in sorted(keywords):
        v = subprocess.check_output(['/usr/sbin/dmidecode', '-s', k]).strip()
        results.append((k, v))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'dmi', ' '.join(result)

