from math import pi


class Pizza:
    def __init__(self, diameter: float, price: float, ingrediens: list[str]) -> None:
        self.diameter = diameter
        self.price = price
        self.ingrediens = ingrediens

    def __str__(self) -> str:
        """
        __str__ Python'a objemizi stringe çevirince ne olması gerektiğini verir.
        Çıktısı str olmalıdır
        """
        return '{}₺ Pizza with {}cm diameter with {}'.format(
            self.price,
            self.diameter,
            ', '.join(self.ingrediens)
        )

    def get_area(self) -> float:
        r = self.diameter / 2
        return r ** 2 * pi

    def __eq__(self, other) -> bool:
        """
        __eq__ Python'ın "==" kıyaslamasında objeyı nasıl kıyaslayacağını gösterir.
        Çıktısı bool olmalıdır.
        """
        if getattr(other, 'get_area'):
            return self.get_area() == other.get_area()
        raise TypeError('You need get_area to do that')

    def __gt__(self, other) -> bool:
        """
        __gt__ Python'ın ">" işleminde objeyi nasıl kıyaslayacağını gösterir.
        Çıktısı bool olmalıdır.
        """
        if getattr(other, 'get_area'):
            return self.get_area() > other.get_area()
        raise TypeError('You need get_area to do that')

    def __lt__(self, other) -> bool:
        """
        __lt__ Python'ın "<" işleminde objeyi nasıl kıyaslayacağını gösterir.
        Çıktısı bool olmalıdır.
        """
        if getattr(other, 'get_area'):
            return self.get_area() < other.get_area()
        raise TypeError('You need get_area to do that')

    def __ge__(self, other) -> bool:
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other) -> list[str]:
        if getattr(other, 'ingrediens'):
            return list(set(self.ingrediens + other.ingrediens))
        raise TypeError('You need get_area to do that')


def main():
    pizza1 = Pizza(26, 60, ['Parmasan', 'Tomato', 'Basil'])
    pizza2 = Pizza(26, 100, ['Pineapple', 'Peperoni', 'Basil'])

    print(pizza1 == pizza2)
    print(pizza1 > pizza2)
    print(pizza1 < pizza2)
    print(pizza1 >= pizza2)
    print(pizza1 <= pizza2)
    print(pizza1 + pizza2)


if __name__ == "__main__":
    main()
