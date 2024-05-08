#!/usr/bin/python3

numbers = []
for i in range(10):
    for j in range(i + 1, 10):
        numbers.append('{:02d}'.format(i * 10 + j))

result = ', '.join(numbers)
print(result)
