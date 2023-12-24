class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def calculate_salary(self, inc: int) -> int:
        return self.age + inc


p1: Person = Person("Pallab", 24)
print(p1.name)

print(p1.calculate_salary(1))
