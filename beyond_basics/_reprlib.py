"""
reprlib supports alternative implementations of repr()
"""
import reprlib  # useful for printing large data

from str_repr import Point2D


points = [Point2D(x, y) for x in range(100) for y in range(100)]

print(len(points))

print(reprlib.repr(points))
