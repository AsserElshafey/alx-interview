#!/usr/bin/python3

import re
import sys
import signal

# Regular expression pattern to match the log line format
log_line_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'
)

# Dictionary to keep track of status code counts
status_code_counts = {str(code): 0 for code in [
    200, 301, 400, 401, 403, 404, 405, 500]}

# Variable to keep track of total file size
total_file_size = 0

# Function to print the metrics


def print_metrics():
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

# Signal handler for keyboard interruption


def signal_handler(sig, frame):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """

    print_metrics()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line_number, line in enumerate(sys.stdin, 1):
        match = log_line_pattern.match(line)
        if match:
            ip, date, status_code, file_size = match.groups()
            total_file_size += int(file_size)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        # Print metrics after every 10 lines or on keyboard interruption
        if line_number % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle any other keyboard interruption
    print_metrics()
    sys.exit(0)
