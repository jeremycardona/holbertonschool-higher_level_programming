#!/usr/bin/python3

output = ""
for i in range(ord('z'), ord('a') - 1, -1):
    if (ord('z') - i) % 2 == 0:
        output += chr(i)
    else:
        output += chr(i - 32)

print("{}".format(output), end="")

