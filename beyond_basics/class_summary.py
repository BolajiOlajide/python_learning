class Foo:
    a_class_attribute = 0

    def __init__(self):
        self.an_instance_attribute = 12
        Foo.a_class_attribute = 100
        self.a_class_attribute = 5  # bad pracctice as this makes an instance
        # attribute instead of overwriting the class attribute

    @staticmethod
    def a_static_method():
        return "No dependency on instance of the class, just lives in class"

    @classmethod
    def a_class_method(cls):
        cls.a_class_attribute += 1

    @classmethod
    def a_named_constructor(cls):
        return cls()

    @property
    def a_property(self):
        return self.an_instance_attribute

    @a_property.setter
    def a_property(self, value):
        self.an_instance_attribute = value
