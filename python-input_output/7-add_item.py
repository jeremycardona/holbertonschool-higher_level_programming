#!/usr/bin/python3
"""add item"""

import sys
import os

import sys
import os


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

file = "add_item.json"
list_items = list(sys.argv[1:])
if os.path.exists(file):
    current_list = load_from_json_file(file)
else:
    current_list = []
current_list += list_items
save_to_json_file(current_list, file)
