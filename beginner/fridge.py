"""Demonstrate raiding a refrigerator."""

from contextlib import closing


class Refrigerator:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == "deep fried pizza":
            raise RuntimeError("Health warning!")  # if we ever get to this
            # block the close operation won't be carried out hence we make
            # use of custom context manager in closing to help and ensure
            # the flow doesn't break.
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door.")


def raid(food):
    with closing(Refrigerator()) as r:
        r.open()
        r.take(food)
        # the close method is called automatically
