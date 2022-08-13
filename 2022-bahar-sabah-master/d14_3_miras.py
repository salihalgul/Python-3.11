class Hayvan:
    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender
        self.alive = True

    def __str__(self) -> str:
        return self.name

    def get_old(self) -> int:
        if self.alive:
            self.age += 1
        return self.age

    def summary(self) -> str:
        return f'{self.name} is a {self.gender}, {self.age} years old animal'


class Kedi(Hayvan):
    def __init__(self, name: str, age: int, gender: str, colors: list[str]) -> None:
        super().__init__(name, age, gender)
        self.colors = colors

    def is_old(self) -> bool:
        if self.age >= 8:
            return True
        return False

    def summary(self) -> str:
        base = super().summary()
        base = base.replace('animal', 'cat')
        base += ' with colors of ' + ', '.join(self.colors)
        return base


class Kopek(Hayvan):
    def __init__(self, name: str, age: int, gender: str, breed: str) -> None:
        super().__init__(name, age, gender)
        self.breed = breed

    def calling(self) -> str:
        gender = 'boy' if self.gender == 'Male' else 'girl'
        return f'{self.name} is a good {gender}!'

    def summary(self) -> str:
        base = super().summary()
        return base.replace('animal', f'{self.breed} dog')


def main() -> None:
    pacchi = Kedi('Pacchi', 2, 'Female', ['Black', 'Brown', 'White'])
    print(pacchi, pacchi.age, pacchi.alive, sep="\n")
    pacchi.get_old()
    print(pacchi.age)
    print(pacchi.summary())

    kont = Kopek('Kont', 8, 'Male', 'German Doberman')
    print(kont.calling())
    print(kont.summary())


if __name__ == "__main__":
    main()
