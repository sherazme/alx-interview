#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""

import sys


i = 0
file_size = 0
status_code = {'200': 0,
               '301': 0,
               '400': 0,
               '401': 0,
               '403': 0,
               '404': 0,
               '405': 0,
               '500': 0}

try:
    for line in sys.stdin:
        arg = line.split(' ')
        if len(arg) > 2:
            line = arg[-2]
            file_size = arg[-1]
            if line in status_code:
                status_code[line] += 1
            file_size += int(file_size)
            i += 1
            if i == 10:
                print('File size: {:d}'.format(file_size))
                sorted_keys = sorted(status_code.keys())
                for key in sorted_keys:
                    value = status_code[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                i = 0
except Exception:
    pass
finally:
    print('File size: {:d}'.format(file_size))
    s_keys = sorted(status_code.keys())
    for key in s_keys:
        value = status_code[key]
        if value != 0:
            print('{}: {}'.format(key, value))
