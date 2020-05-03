"""
Decorators are a way to modify or enhance functions
w/o changing their definition.
"""
# functions as decorators


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def vegetable():
    return "blomkåi"


@escape_unicode
def animal():
    return "bjørn"


@escape_unicode
def mineral():
    return "stål"


print(vegetable())
print(animal())
print(mineral())
