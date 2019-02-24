# dictionaries can be created by passing data strcuctures with pairs such
# as 2-itemed tuples to the dict constructor
ran = [('Alice', 20), ('Jane', 34), ('Sophia', 19)]
d = dict(ran)
print(d)

# or passing keyword args to the dict constructor
e = dict(wheat=0xD423AB, flour=0x1234CCD)
f = dict(e)
print(f)

# dictionaries can be copied by calling the copy method
g = f.copy()
print(g)
print(g is f)
print(g == f)

# or passing the dictionary to the dict constructor
h = dict(d)
print(h)
print(h is d)
print(h == d)

# dictionaries can be updated/extended with the update method
h.update(g)
print(h)
print()

# if you need to iterate over only the values in a dictionary
# you can use the values() function
for i in h.values():
    print(i)
    print()

for key, value in g.items():
    print("key => {}, value => {}".format(key, value))