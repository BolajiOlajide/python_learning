# use enumerate keyword when you need something to serve as a counter
a = list(range(5,20,2))

for _ in enumerate(a):
    print(_)
    # this returns
    # (0, 5)
    # (1, 7)
    # (2, 9)
    # (3, 11)
    # (4, 13)
    # (5, 15)
    # (6, 17)
    # (7, 19)


# making use of tuple unpacking, you can grab the counter and the value
for i, v in enumerate(a):
    print("count = {}, value = {}".format(i,v))
    # This returns
    # count = 0, value = 5
    # count = 1, value = 7
    # count = 2, value = 9
    # count = 3, value = 11
    # count = 4, value = 13
    # count = 5, value = 15
    # count = 6, value = 17
    # count = 7, value = 19