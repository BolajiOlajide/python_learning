def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=False)

t = seq("Timbuktu")
print(t)
print(type(t))