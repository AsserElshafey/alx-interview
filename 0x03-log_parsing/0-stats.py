#!/usr/bin/python3

import re
import sys
import signal


# Define the regular expression pattern for the log line
log_line_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)'
)

# Initialize a dictionary to count status codes
status_code_counts = {str(code): 0 for code in [
    200, 301, 400, 401, 403, 404, 405, 500]}

# Initialize the total file size
total_file_size = 0


def print_metrics():
    """Print the metrics for file size and status code counts."""
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_metrics()
    sys.exit(0)


# Register the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Process the input line by line
try:
    for line_number, line in enumerate(sys.stdin, start=1):
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
