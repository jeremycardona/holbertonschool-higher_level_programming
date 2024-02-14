class Fruit:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"i am a: {self.name}"

    def __repr__(self):
        return self.color
# print(repr)
m = Fruit("yellow", "banana")
print(m)
print()

b = m.__repr__()
print(b)
