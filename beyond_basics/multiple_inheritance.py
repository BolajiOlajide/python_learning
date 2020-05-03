class Base1:
    def __init__(self):
        print("Base1.__init__")


class Base2:
    def __init__(self):
        print("Base2.__init__")


class Base3(Base1, Base2):
    """
    If a class inherits multiple classes and defines no __init__ method,
    the __init__ method of the first base class is called. The others aren't called.
    """

    pass


b3 = Base3()
print(Base3.__bases__)  # check the base classes a class inherits from
print(Base1.__bases__)
print("===================================================")

# to check the MRO (Method Resolution Order) for a class, you can use the __mro__ Method
print(Base3.__mro__)  # or Base3.mro()
# MRO is the ordering of a class's inheritance graph that python calculates for you.
