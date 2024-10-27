#!/usr/bin/python3
"""
This script reads log lines from standard input, validates them, and keeps\
    track of statistics.

The log lines are expected to be in the format:
    <IP Address> - - [<Date>] "GET /projects/260 HTTP/1.1" <Status Code> <File\
        Size>

The script maintains a count of the total file size and the number of\
    occurrences of each status code.
Every 10 lines, it prints the current statistics.

Functions:
    check_line(line): Validates if a line is a proper log line.

Variables:
    i (int): Counter for the number of lines processed.
    stats (defaultdict): Dictionary to store the statistics.

Exceptions:
    KeyboardInterrupt: Handles the interruption to print the final statistics\
        before exiting.
"""
from collections import defaultdict
from sys import stdin
import regex as re


def check_line(line):
    """
    Check if line is a valid log line

    Args:
        line (str): line to check

    Returns:
        bool: True if line is valid, False otherwise
    """
    ip, rest = line.split(" - ")
    if not re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip):
        return False
    rest = rest.split(" ")
    return (
        len(rest) == 7
        and re.match(
            r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]",
            " ".join(rest[:2]),
        )
        and re.match(r"\"GET /projects/260 HTTP/1.1\"", " ".join(rest[2:5]))
        and re.match(r"\d{3}", rest[5])
        and re.match(r"\d+", rest[6])
    )


i = 0
stats = defaultdict(int)
try:
    while True:
        line = stdin.readline()
        if check_line(line):
            stats["size"] += int(line.split(" ")[-1])
            stats[f"{line.split(' ')[-2]}"] += 1
        i += 1
        if i % 10 == 0:
            print(f"File size: {stats['size']}")
            for k, v in sorted(stats.items()):
                if k != "size" and v != 0:
                    print(f"{k}: {v}")
except KeyboardInterrupt as e:
    print(f"File size: {stats['size']}")
    for k, v in sorted(stats.items()):
        if k != "size" and v != 0:
            print(f"{k}: {v}")
    raise e
