from math import factorial
from pprint import pprint as pp

words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

# a list comprehension is enclised in square brackers
print([len(word) for word in words])

# [ expr(item) for item in iterable]


# Set comprehension
print({len(str(factorial(x))) for x in range(20)})



# Dictionary comprehension
# This takes this format { key_expr: value_expr for item in iterable}
country_to_capital = {
    'United Kingdom': 'London',
    'Brazil': 'Brazilia',
    'Morocco': 'Rabat',
    'Sweden': 'Stockholm'
}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
pp(capital_to_country)