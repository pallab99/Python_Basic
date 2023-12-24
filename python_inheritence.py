class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def calculate_salary(self, inc: int) -> int:
        return self.age + inc


class Pallab(Person):
    pass


p1: Person = Person("Pallab", 24)
p2: Pallab = Pallab("Pallab", 28)
print(p2.age, p2.name)
