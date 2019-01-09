# Classes as decorators


class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print('hello {}'.format(name))


print(hello('Bolaji'))
print(hello('Proton'))
print(hello('Moto'))
print(hello.count)
