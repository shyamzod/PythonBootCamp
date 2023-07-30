class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  class InnerClass:
    def __init__(self):
      print("Helloworld")
p1 = Person("John", 36)
print(p1.name)
print(p1.age)


class Day1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Day1("John", 36)

print(p1.name)
print(p1.age)
