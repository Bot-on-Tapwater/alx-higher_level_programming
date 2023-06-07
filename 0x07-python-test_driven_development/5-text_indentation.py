#!/usr/bin/python3
"""
Inserts double newline after "." "?" ":"
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    result = ""
    line = ""

    for char in text:
        line += char
        if char in punctuation:
            result += line.strip() + "\n\n"
            line = ""

    if line:
        result += line.strip()

    print(result, end="")
