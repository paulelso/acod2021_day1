#!/usr/bin/env python3
input_s = '''\
199
200
208
210
200
207
240
269
260
263
'''

numbers = [int(line) for line in input_s.splitlines()]
    
count = sum(
    numbers[i] > numbers[i - 1]
    for i in range(1, len(numbers))
)

print(f'PART 1 - Number of increases {count}.')

count = sum(
    numbers[i] > numbers[i - 3]
    for i in range(3, len(numbers))
)

print(f'PART 2 - Number of increases {count}.')
