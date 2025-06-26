#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys


def print_stats(file_size, status_codes):
    """
    Print the accumulated metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    file_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.strip().split()
                status = int(parts[-2])
                size = int(parts[-1])

                file_size += size
                if status in status_codes:
                    status_codes[status] += 1

            except (IndexError, ValueError):
                # Ignore lines that don't match the format
                continue

            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        # Print before exiting on Ctrl+C
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)
