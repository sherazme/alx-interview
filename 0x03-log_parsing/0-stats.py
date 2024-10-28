#!/usr/bin/python3

import sys


def display_msg(status_code, total_size):
    """ print message """

    print("File size: {}".format(total_size))
    for key, val in sorted(status_code.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
code = 0
count = 0
status_code = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_code.keys()):
                    status_code[code] += 1

            if (count == 10):
                display_msg(status_code, total_size)
                count = 0

finally:
    display_msg(status_code, total_size)
