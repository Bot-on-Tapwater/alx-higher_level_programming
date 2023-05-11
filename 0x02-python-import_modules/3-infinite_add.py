#!/usr/bin/python3
import sys
counter = 0
sum = 0

if __name__ == '__main__':
    for args in sys.argv:
        if (len(sys.argv) == 1):
            print("{:d}".format(sum))
        else:
            if (counter != 0):
                sum += int(args)
            counter += 1
    print("{:d}".format(sum))
