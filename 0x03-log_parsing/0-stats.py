#!/usr/bin/python3
"""
    Module implementing functions that read from standard input
    and computes metrics from the input

"""
import sys
import signal


total_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

line_count = 0


def print_stats():
    """Prints log statistics"""
    print(f"File size: {total_file_size}")
    for code, code_count in status_codes.items():
        if code_count > 0:
            print(f"{code}: {code_count}")


def handle_signal(sig, frame):
    """Handles the interrupt signal from crtl + C"""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, handle_signal)


def print_metric():
    """Parses and prints metrics from stdin"""
    global total_file_size
    global line_count
    for line in sys.stdin:
        try:
            metrics = line.strip().split()
            # print(f"{len(metrics)}: {metrics}")
            if len(metrics) != 9:
                continue
            ip = metrics[0]
            dash = metrics[1]
            date = metrics[2]
            method = metrics[4]
            url = metrics[5]
            protocol = metrics[6]
            status_code = metrics[7]
            file_size = metrics[8]

            if dash != '-' or not date.startswith('[') or method != '"GET'\
                    or url != '/projects/260' or protocol != 'HTTP/1.1"':
                continue
            # status_code = int(status_code)
            file_size = int(file_size)

            if status_code in status_codes.keys():
                status_codes[status_code] += 1

            total_file_size += int(file_size)
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except Exception as e:
            continue

    print_stats()


if __name__ == "__main__":
    print_metric()
