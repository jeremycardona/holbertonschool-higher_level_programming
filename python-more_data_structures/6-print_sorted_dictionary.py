#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary.keys())

    for k in sort_dic:
        print(f"{k}: {sort_dic.values()}")
