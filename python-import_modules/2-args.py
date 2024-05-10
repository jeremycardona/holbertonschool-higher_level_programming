#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num_arg = len(argv) - 1
    if num_arg == 0:
        print("{} arguments.".format(num_arg))
    if num_arg == 1:
        print("{} argument.".format(num_arg))
        print("{}: {}".format(num_arg, argv[1]))
    else:
        print("{} arguments:".format(num_arg))
        for i in range(1, num_arg + 1):
            print("{}: {}".format(i, argv[i]))
