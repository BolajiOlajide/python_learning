# to run a function on a collection (every single item in it)
# you can make use of the map method

ords = map(ord, 'The quick brown fox')
print(ords, '\n')

# map() is lazy - it only produces values as they're needed
# the result of map is a generator object

# to get all the output of the generator object you can simply
# convert to a string
list_of_ords = list(ords)
print(list_of_ords)
