from math import pi


def get_input(text: str) -> float:
    user_input = input(text + ': ')
    try:
        return float(user_input)
    except ValueError:
        print(f'Please provide a number.\n "{user_input}" is not a number')
        return get_input(text)


class Pizza:
    def __init__(self, size: str, diameter: float, price: float) -> None:
        self.size = size
        self.diameter = diameter
        self.price = price
        self.area = self.get_area()
        self.score = self.get_score()

    def __str__(self) -> str:
        return f"{self.size} pizza with score of {self.score:.2f}"

    def get_area(self) -> float:
        r = self.diameter / 2
        area = pi * r ** 2
        return area

    def get_score(self) -> float:
        return self.area / self.price


def create_pizza(size: str) -> Pizza:
    diameter = get_input(f"Diameter of {size} Pizza")
    price = get_input(f"Price of {size} Pizza")
    return Pizza(size, diameter, price)


def main():
    small_pizza = create_pizza("Small")
    large_pizza = create_pizza("Large")

    print(f"SCORES:\n\t{small_pizza}\n\t{large_pizza}")

    if small_pizza.score > large_pizza.score:
        print("Winner is Small Pizza")
    elif small_pizza.score < large_pizza.score:
        print("Winner is Large Pizza")
    else:
        print("Congratulations, your pizza place is being runned by a math professor!")


if __name__ == "__main__":
    main()
