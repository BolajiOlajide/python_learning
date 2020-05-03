from timeit import timeit

time_taken = timeit(
    setup="from random import randrange", # stuff to import and shit
    stmt="[randrange(s) for s in range(100, 1000)]", # operation to run
    number=100, # numebr of times to run said operation ☝🏽
)
print(f'time taken is {time_taken}')
