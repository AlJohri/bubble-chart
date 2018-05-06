#!/usr/bin/env python3

import sys
import csv

reader = csv.reader(sys.stdin)
writer = csv.writer(sys.stdout)

header = next(reader)
writer.writerow(['id', 'value'])
writer.writerow(['root',''])

for row in reader:
    row[0] = 'root.' + row[0]
    writer.writerow(row)
