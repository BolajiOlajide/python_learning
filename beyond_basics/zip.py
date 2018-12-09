from pprint import pprint as pp


monday = [23, 24, 56, 90, 18, 21, 23, 19]
tuesday = [8, 11, 34, 55, 49, 23, 99, 88]
sunday = [10, 20, 19, 14, 26, 41, 29, 38]

for item in zip(sunday, monday, tuesday):
    print(item)

print('===================')
daily = [sunday, monday, tuesday]

for item in zip(*daily):
    pp(item)

print('===================')

transposed = list(zip(*daily))
print(transposed)
