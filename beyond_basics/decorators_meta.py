"""
When you define decorators, they replace the meta data of the functions
they wrap i.e the __name__ of the wrappped function will be pointing to
that of the decorator and other internal method.

The way to bypass this is by manually specifying this in the decorator
decorator.__name__ = f.__name__
decorator.__doc__ = f.__doc__

or by using the functools.wraps function - it properly updates metadata on
wrapped functions
"""
import functools


def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper


@noop
def hello():
    """Prints the word, hello"""
    return 'Hello'


print(hello.__name__)
print(hello.__doc__)


# To parameterize decorators you need a function that creates decorators
def check_something(x):
    # check that a certain word is passed as argument
    def validate(f):
        @functools.wraps(f)
        def wraps(*args):
            if x in args:
                raise ValueError(
                    '{} should not be part of the args'.format(x)
                )
            return f(*args)
        return wraps
    return validate


@check_something('name')
def init(*args):
    return True


print(init('Bolaji', 'James', 'Prowse', 'Ole Gunnar Solksjaer'))
print(init('love', 'name'))