s = "show how to index into sequences".split()

print(s)
print()
print(s[4])

# you can access the indexes backward
# if you need to get the fifth element from the back you can do
print(s[-5])

# slicing is a fomr of extended indexing
print(s[1:4])

# to slice the array and take every element except the first and last
print(s[1:-1])

# sorting accepts two optional args
# reverse and true
h = 'I am not dangerous player'.split()

h.sort(key=len) # sorting by the length of each word using the len function
print(h)

h.sort(reverse=True)
print(h)