iterable = ['Spring', 'Summer', 'Autumn', 'Winter']

iterator = iter(iterable)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print('Items finished in the iterable!')


def gen123():
    yield 1
    yield 2
    yield 3
    return

g = gen123()

print(next(g))
print(next(g))

# an example of a generator comprehension
million_squares = (x * x for x in range(1,10002))
print(million_squares)
print(next(million_squares))
print(next(million_squares))
print(next(million_squares))
print(next(million_squares))
print()


# zip is also a userful tool
a = [2,3,4,32,2,3,6,764,2,223,4,54,31,234,5]
b = [1,2,5,6,3,2,3,5,6,8,9,7,5,3,2]

for i in zip(a,b):
    print("The min is {:4.1f}, max ids {:4.1f} while the average is {:4.1f}"
          .format(min(i), max(i), (sum(i) / len(i))))

# the built in any method and all method are used to perform memory efficient calculations
# the any method returns true if any of the conditions are true while the all returns True if
# all the conditions are True otherwise False.

print()
print(any(t > 0 for t in (1,2,3,4,5)), 'should be equal to True')
print(any(t > 0 for t in (1,2,3,-4,5)), 'should be equal to True')
print(any(t == 10 for t in (1,2,3,-4,5)), 'should be equal to False')
print()
print(all(t > 0 for t in (1,2,3,4,5)), 'should be equal to True')
print(all(t > 0 for t in (1,2,3,-4,5)), 'should be equal to False')
print()
