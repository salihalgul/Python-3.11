class Deneme:
    name: str = ''
    surname: str = ''
    age = 0

    def say_hello(self):
        print(f"Hello {self.name}!")

    def get_old(self):
        self.age += 1


mahmut = Deneme()

print(mahmut.name)
mahmut.name = 'Mahmut'
mahmut.say_hello()
print(mahmut.name)
print("-" * 20)

print(mahmut.age)
mahmut.get_old()
print(mahmut.age)


print("-" * 20)


class Student:
    """
    This is a random class that accepts those agrs:
    name: String
    surname: String
    age: Integer
    subject: String
    """

    def __init__(self, name: str, surname: str, age: int, subject: str) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.subject = subject

    def __str__(self) -> str:
        return self.get_full_name()

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def get_old(self) -> None:
        self.age += 1


salih = Student("Salih", "Algül", 46, "Python")
print(salih.name, salih.surname, salih.age, salih.subject)
print(salih)
salih.get_old()
print(salih.age)

fatih = Student("Fatih", "Özaydın", 30, "Python")
print(fatih, fatih.age)
fatih.get_old()
print(fatih.age)
