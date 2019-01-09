# LEGB rule
# Local, Enclosing, Global, Built-in


def outer():
    x = 3

    def inner(y):
        return x + y

    return inner


# closures can be accessed with the __closure__ method
i = outer()
print(i.__closure__)
print(i(5))


def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


square = raise_to(2)
print(square.__closure__)
print(square(3))

# LEGB does not apply when making new bindings

"""
The global keyword is used to introduce a global variable
into the local namespace.

The nonlocal keyword is used to introduce names from
the enclosing namespace into the local namespace.
"""
