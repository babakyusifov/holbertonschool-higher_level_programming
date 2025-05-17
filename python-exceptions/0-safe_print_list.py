#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        len_list = 0
        for i in range(0, x):
            print(my_list[i], end='')
            len_list += 1
        print()
    except (IndexError, TypeError):
        print()
    return len_list

