class Example:
    MAX_AGE = 40

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > Example.MAX_AGE:
            raise ValueError('You are way too old, lol.')
        self._age = value


e = Example('Jone Doe', 50)

print(e.name)
print(e.age)

# e.age = 55  # this would result in a value error

print(e.age)
