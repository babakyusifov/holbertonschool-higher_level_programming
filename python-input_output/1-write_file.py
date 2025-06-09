#!/usr/bin/python3
"""This module contains a function to write a
UTF-8 text file."""


def write_file(filename="", text=""):
    """write a UTF-8 text file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
