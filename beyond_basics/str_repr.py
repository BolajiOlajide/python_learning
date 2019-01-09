class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # intended to provide readable, human-friendly
        # representation of an object
        # by default - str() calls repr() if the str() is defined
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        # repr - produces an unambiguous string
        # representation of an object.
        # Generally speaking - the repr() should contain more
        # information than the result of str()
        return 'Point2D(x={}, y={})'.format(self.x, self.y)
