def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = ""
    for char in text:
        new_line += char
        if char in ".?:":
            print(new_line.strip())
            print()
            new_line = ""

    if new_line.strip():
        print(new_line.strip())

