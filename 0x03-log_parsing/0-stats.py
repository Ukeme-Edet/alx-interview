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
from sys import stdin, stdout
import ipaddress
import datetime


def print_stats(stats):
    """
    Print Stats

    Args:
        stats (dict): dictionary of stats
    """
    print("File size: {}".format(stats["File size"]))
    for key in sorted(stats.keys()):
        if key != "File size" and stats[key] != 0:
            print("{}: {}".format(key, stats[key]))


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
        if not valid_line(line):
            pass
        data = line.split()
        stats[data[-2]] += 1
        stats["File size"] += int(data[-1])
        line_count += 1
        if line_count == 10:
            print_stats(stats)
            line_count = 0
except KeyboardInterrupt:
    print_stats(stats)
