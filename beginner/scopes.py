"""
Demonstrate scoping (global)
"""

count = 0

def show_count():
    print('count = ', count)


def set_count(c):
    global count # if we don't set the count to reflect on the global variable count the change won't reflect
    count = c
