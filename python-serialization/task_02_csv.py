#!/usr/bin/python3
"""Module that converts csv data to json format"""
import csv
import json


def convert_csv_to_json(csv):
    """convert csv file to json format"""
    try:
        with open(csv, mode="r") as csv_file:
            read = csv.DictReader(csv_file)
            data = [row for row in read]

        with open("data.json", mode="w") as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        print(f"Error: {Exception}")
        return False
