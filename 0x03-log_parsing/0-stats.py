#!/usr/bin/python3
"""
Log parsing
"""

import sys

status_codes = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}
file_size = 0
line_count = 0

def print_stats():
    """Prints accumulated stats"""
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) >= 7:
            status = parts[-2]
            size = parts[-1]

            if status in status_codes:
                status_codes[status] += 1
            try:
                file_size += int(size)
            except Exception:
                pass

            line_count += 1
            if line_count % 10 == 0:
                print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

# If file ends normally
print_stats()

