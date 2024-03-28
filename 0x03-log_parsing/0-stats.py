#!/usr/bin/python3
""" Module for 0-stats"""

import sys
from collections import Counter


def print_stats(total_size, status_counts):
    """
    Prints the current statistics:
    total file size and status code counts.
    """

    print(f"Total file size: {total_size}")
    for code, count in sorted(status_counts.items()):
        print(f"{code}: {count}")


total_size = 0
status_counts = Counter()
line_count = 0

try:
    for line in sys.stdin:
        parts = line.strip().split()

        if len(parts) != 6 or not parts[4].isdigit() or not parts[5].isdigit():
            continue

        total_size += int(parts[5])
        status_counts[int(parts[4])] += 1

        line_count += 1

        if line_count % 10 == 0 or line_count == 1:
            print_stats(total_size, status_counts)
            total_size = 0
            status_counts.clear()

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)
