#!/usr/bin/env python
import sys

memory = []
memory_size = 10000

file_count = 10
temp_dir = "temp"
data_dir = "data"

def check_memory():
    if len(memory) > memory_size:
        return False
    return True

for i in range(file_count):
    memory = []
    with open("%s_gen.data" % (i + 1)) as f:
        for line in f:
            memory.append(int(line.strip()))
            if not check_memory():
                print("memory exploded!!!")

    with open("%s/%s.data" % (temp_dir, (i + 1)), 'w+') as f:
        memory = sorted(memory)
        for m in memory:
            f.write("%s\n" % m)

files = []
part_index = 1
for i in range(file_count):
    files.append(open("%s/%s.data" % (temp_dir, (i + 1))))

cache = []
for f in files:
    cache.append(int(f.readline().strip()))
memory = []
while files:
    index = sorted(range(len(cache)), key = lambda k : cache[k])
    memory.append(cache[index[0]])
    new_data = files[index[0]].readline()
    if new_data:
        cache[index[0]] = int(new_data)
    else:
        files.pop(index[0])
        cache.pop(index[0])

    if len(memory) == memory_size:
        with open("%s/part_%s.data" % (data_dir, part_index), "w+") as wf:
            for m in memory:
                wf.write("%s\n" % m)
        memory = []
        part_index += 1


