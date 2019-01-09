"""
@staticmethod vs @classmethod

@staticmethod
- No access needed to either class or instance objects
- most likely an implementation detail of the class
- may be able to tbe moved to become a module-scope function

@classmethod
Requires access to the class object to call other class
methods or the constructor
"""


class ShippingContainer:

    next_serial = 1337

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()


c1 = ShippingContainer('MAE', 'clothes')
print(c1.serial)

c2 = ShippingContainer('WOL', 'tools')
print(c2.serial)

c3 = ShippingContainer.create_empty('YME')
print(c3.serial)

c4 = ShippingContainer.create_with_items('ONE', ('Rice', 'Beans', 'Egusi'))
print(c4.serial)
print(c4.contents)
