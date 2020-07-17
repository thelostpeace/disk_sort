#!/usr/bin/env python
import random

file_count = 10
file_name = "%s_gen.data"
count = 10000
low = 10
high = 100000

for i in range(file_count):
    with open(file_name % (i + 1), 'w+') as f:
        for k in range(count):
            f.write("%s\n" % random.randint(low, high))
