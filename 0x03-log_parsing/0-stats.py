#!/usr/bin/python3
"""
Log Parsing

Reads stdin line by line and computes metrics

Metrics:
    - Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <stat\
us code> <file size>
    - After every 10 lines and/or a keyboard interruption (CTRL + C), print th\
ese statistics from the beginning:
        - Total file size: File size
        - Status code: 200, 301, 400, 401, 403, 404, 405, 500
        - Format: <status code>: <number>
        - Status codes should be printed in ascending order
"""
from sys import stdin
import ipaddress
import datetime


def print_stats(stats):
    """
    Print Stats

    Args:
        stats (dict): dictionary of stats
    """
    out = "File size: {}".format(stats["File size"])
    for key in sorted(stats.keys()):
        if key != "File size" and stats[key] != 0:
            out += "\n{}: {}".format(key, stats[key])
    print(out)


def valid_line(line):
    ip = line.split("-")[0].strip()
    date = line.split("[")[1].split("]")[0].strip()
    request = '"' + line.split('"')[1] + '"'
    status = line.split()[-2]
    file_size = line.split()[-1]
    try:
        ipaddress.ip_address(ip)
        datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f")
        int(file_size)
    except ValueError:
        return False
    return request == '"GET /projects/260 HTTP/1.1"' and status in [
        "200",
        "301",
        "400",
        "401",
        "403",
        "404",
        "405",
        "500",
    ]


stats = {
    key: 0
    for key in [
        "200",
        "301",
        "400",
        "401",
        "403",
        "404",
        "405",
        "500",
        "File size",
    ]
}
line_count = 0
try:
    for line in stdin:
        line_count += 1
        if not valid_line(line):
            continue
        line = line.split()
        stats["File size"] += int(line[-1])
        stats[line[-2]] += 1
        if line_count == 10:
            print_stats(stats)
            line_count = 0
    print_stats(stats)
except (KeyboardInterrupt, EOFError):
    print_stats(stats)
    raise
