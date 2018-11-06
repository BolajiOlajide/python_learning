"""
A module for demonstrating exceptions.
"""

def _convert(s):
    ''' convert to an integer.  without handling exception'''
    x = int(s)
    return x


def convert(s):
    ''' convert to an integer.  with handling exception'''
    try:
        x = int(s)
    except ValueError:
        x = -1
    return x
