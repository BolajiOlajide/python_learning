scientists = [
    'Marie Curie',
    'Albert Einstein',
    'Niels Bohr',
    'Isaac Newton',
    'Dmitri Mendeleev',
    'Antoine Lavoisier',
    'Carl Linna',
    'Alfred Wegener',
    'Charles Darwin'
]

print(sorted(scientists, key=lambda name: name.split()[-1]))

last_name = lambda name: name.split()[-1]  # noqa: E731
print(last_name("Bolaji Olajide"))

# Difference between a lambda and a def function

# A def function is a statement which defines a function and binds it to a
# name while a lambda is an expression which evaluates to a function.

# A def function must have a name while a lambda is anonymous.

# The arguments in a def function are delimited by parentheses, separated by
# commas while for lambdas the argument list is terminated by a colon and
# separated by commas

# the body of a regular function is an indented block of statements while
# the body of a lambda is a single function

# a return statement is required to return anything in a regular def function
# while the return value for a lambda is given by the body expression - infact
# no return statement is permitted

# regular functions can have docstrings while lambdas can't.

# regular functions are easy to test but lambdas are awkward to test
# considering they're anonymous.
