import sys
import os

class SysDir (dict):

    def __init__ (self, path, alsoprocess=None):
        self.path = path

        for k in os.listdir(self.path):
            kpath = os.path.join(self.path, k)
            if not os.path.isfile(kpath):
                continue

            try:
                self[k] = open(kpath).read().strip()
            except IOError:
                pass

        if alsoprocess:
            for k in alsoprocess:
                self[k] = SysDir(os.path.join(self.path, k))

if __name__ == '__main__':
    d = SysDir(sys.argv[1], alsoprocess=sys.argv[2:])

