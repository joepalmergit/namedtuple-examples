from collections import namedtuple

Person = namedtuple("Person", ["first_name", "last_name"])

p = Person("Liam", "Howlett")
p_2 = Person("Keith", "Flint")

print(p.first_name)
print(p.last_name)

print(p_2.first_name)
print(p_2.last_name)
