#!/usr/bin/python3

"""
Read from stdin and compute metrics
"""

import sys
import signal

total_file_size = 0
status_code_counts = {}


def print_statistics(signal, frame):
    """
    Prints statistics
    """
    global total_file_size, status_code_counts
    print("File size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print("{}: {}".format(code, status_code_counts[code]))
    if signal is not None:
        sys.exit(0)


signal.signal(signal.SIGINT, print_statistics)

line_count = 0
for line in sys.stdin:
    line_count += 1
    parts = line.split(" ")
    status_code = int(parts[-2])
    file_size = int(parts[-1])

    total_file_size += file_size
    if status_code in status_code_counts:
        status_code_counts[status_code] += 1
    else:
        status_code_counts[status_code] = 1

    if line_count % 10 == 0:
        print_statistics(None, None)
