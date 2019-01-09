# instances as decorators


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()


@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


lol = [1, 2, 3]
lol = rotate_list(lol)
print(lol)
lol = rotate_list(lol)
print(lol)
lol = rotate_list(lol)
print(lol)

tracer.enabled = False

lol = rotate_list(lol)
print(lol)
lol = rotate_list(lol)
print(lol)
