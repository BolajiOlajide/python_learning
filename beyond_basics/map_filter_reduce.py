from functools import reduce
import operator

mul = lambda x: x * 2
items = [1, 2, 4, 5, 6, 8, 9, 10]

print(map(mul, items))  # [4, 8, 12, 16, 20]
# if you are using python3 then the result of map and filter will
# be lazy loaded so you have to manually convert to a list

first_names = ["John", "Jane", "James", "Jacob", "Jennifer"]
last_names = ["Doe", "Wash", "McClean", "James"]

print()

is_odd = lambda x: not (x % 2)
print(filter(is_odd, items))  # [2, 4, 6, 8, 10]

mul_2 = lambda x, y: x * y

new_items = [1, 2, 3, 4, 5]

print(reduce(mul_2, new_items))  # 120
print(reduce(operator.add, new_items))  # 15
