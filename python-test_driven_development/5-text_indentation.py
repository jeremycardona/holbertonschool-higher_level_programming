#!/usr/bin/python3
"""Print function for a text with 2 new lines"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':' """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in ".?:":
        text = (delimeter + "\n\n").join(
            [line.strip(" ") for line in text.split(delimeter)])

    print(text, end="")
