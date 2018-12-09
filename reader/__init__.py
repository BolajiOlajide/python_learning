"""
Sample doc for reader module.

Just testing this out.
"""
from reader.reader import Reader
print('reader is imported')

# this is used to specify the modules to be imported when the user does
# from reader import *.
# if this isn't specified then
__all__ = [Reader]
