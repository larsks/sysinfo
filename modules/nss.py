#!/usr/bin/python

def probe():
    results = []

    for line in open('/etc/nsswitch.conf'):
        if not line.strip() or line.startswith('#'):
            continue

        map, modules = line.strip().split(':', 1)

        results.append((map.strip(), modules.strip()))

    return results

if __name__ == '__main__':
    for result in probe():
        print 'nss', ' '.join(result)

