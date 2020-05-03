class Base:
    def __init__(self):
        print("Base initializer")

    def f(self):
        print("Base.f()")


class Sub(Base):
    def __init__(self):
        super().__init__()  # we have to explicitly call the base class's initializer
        print("Sub initializer")

    def f(self):
        super().f()  # same for every other overriden method you want to extend
        print("Sub.f()")
