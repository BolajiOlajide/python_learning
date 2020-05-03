# Feels like almost everything in python is callable


# normal functions are callable
def is_even(x):
    return True if x % 2 == 0 else False


print("callable(is_even) = {}".format(callable(is_even)))


# lambdas are callable
is_odd = lambda x: x % 2 != 0  # noqa: E731


print("callable(is_odd) = {}".format(callable(is_odd)))


# classes are callable
print("callable(list) = {}".format(callable(list)))


# methods are callable
print("callable(list.append) = {}".format(callable(list.append)))


class CallMe:
    def __call__(self):
        print("Called!")


c = CallMe()
print("callable(c) = {}".format(callable(c)))


# strings aren't callable
print("callable('Random String') = {}".format(callable("Random String")))
