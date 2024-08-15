#!/usr/bin/python3
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """Handles the CTRL + C signal."""
    print_stats()
    sys.exit(0)

# Bind the signal handler to CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if the line has the correct format
        if len(parts) != 7:
            continue

        ip_address, dash, date, method, url, status_code, file_size = parts

        # Check if the method is GET and the URL matches
        if method != '"GET' or url != '/projects/260':
            continue

        # Update total file size
        try:
            total_size += int(file_size)
        except ValueError:
            continue

        # Update status code count
        if status_code in status_codes:
            status_codes[status_code] += 1

        # Print stats after every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    pass
finally:
    # Final stats when the program ends
    print_stats()

