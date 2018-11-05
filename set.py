# to create an empty set you must use the set constructor

e = set()
print(e)

p = {9,23,239,4,1,0,90}
print(p)
print(type(p))

# to add a single element to a set use the add() method
p.add(1000)
print(p)

# multiple elements can be added in one go
p.update([37, 128, 97, 9])
print(p)

# to remove an element from a set you can use one of two methods
# - remove() method
# removes the element in the set but throws an error if the element
# doesn't exist
p.remove(9)

try:
    # throws an error if the element doesn't exist
    p.remove(800)
except KeyError:
    print('Just encountered a key error')


# - discard method
# removes the element in the set and doesn't throw an error if element
# doesn't exist
p.discard(128)
p.discard(129)
print(p)

# set also makes use of the copy method for shallow copying
k = p.copy()
# or using the set constructor
l = set(p)

print(k is p)
print(l is p)
print(k == p)
print(l == p)

# SETS A used most times for the set algebra - venn diagram kini
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# to see everyone who are in either or both of two sets you
#  can use the union method
print(blue_eyes.union(blond_hair))

# to get the set that satisfies two condition we can use the intersection
# method. For example to get people with blue eyes and blond hair
print(blue_eyes.intersection(blond_hair))

# to identify the people with blond hair who don't have blue eyes
print(blond_hair.difference(blue_eyes))

# use the symmetric_difference() method to get people with blond hair or
# blue eyes exclusively but not both
print(blond_hair.symmetric_difference(blue_eyes))

# you can can check if a set is a sub set of another.
# for instance we can check if all the people who can smell_hcn have blond hair
print(smell_hcn.issubset(blond_hair))

# you can also use the issuperset() method to check if a set is a superset
# of another
print(taste_ptc.issuperset(smell_hcn))

# you can also test if two sets have no members in common i.e they're disjointed
print(a_blood.isdisjoint(b_blood))
