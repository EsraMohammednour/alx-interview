#!/usr/bin/python3
'''log parsing
'''
import sys
import signal
import re


def signal_handler(sig, frame):
    '''signal handler'''
    print_metrics()
    sys.exit(0)


def print_metrics():
    '''print metrics'''
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


line_count = 0
file_sizes = []
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
status_codes_count = {code: 0 for code in status_codes}

p = re.compile(r'^([\d.]+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        match = p.match(line)
        if not match:
            continue
        groups = match.groups()
        file_size = int(groups[2])
        status_code = int(groups[1])
        file_sizes.append(file_size)
        if status_code in status_codes:
            status_codes_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_metrics()
except KeyboardInterrupt:
    print_metrics()
