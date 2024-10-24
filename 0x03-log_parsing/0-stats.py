#!/usr/bin/python3
import sys
import signal
import re


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.'''
    p = re.compile(
            r'^([\d.]+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    )
    match = p.match(input_line)
    if match:
        groups = match.groups()
        return int(groups[1]), int(groups[2])
    return None, None


def print_statistics(total_file_size, status_codes_count):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f'{code}: {status_codes_count[code]}')


def signal_handler(sig, frame):
    '''Signal handler'''
    print_statistics(sum(file_sizes), status_codes_count)
    sys.exit(0)


line_count = 0
file_sizes = []
status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
status_codes_count = {code: 0 for code in status_codes}

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        status_code, file_size = extract_input(line)
        if status_code is not None and status_code in status_codes:
            file_sizes.append(file_size)
            status_codes_count[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_statistics(sum(file_sizes), status_codes_count)


except KeyboardInterrupt:
    print_statistics(sum(file_sizes), status_codes_count)
