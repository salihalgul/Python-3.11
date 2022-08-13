"""
Bu programımız kullanıcıdan aldığı inputlar ile oluşturduğu iki pizzayı birbiri ile
kıyaslayıp fiyat/performans olarak hangisinin daha verimli olduğunu belirleyecek.

Bu program içerisinde sizden birkaç tane fonksiyon yazmanızı isteyeceğim.
1- get_input: Kullanıcıdan input alıp bunu işleyecek fonksiyon.
2- create_pizza: Kullanıcıdan aldığı input ile pizza oluşturacak fonksiyon.
* Pizza içeriği olarak sadece çapı ve fiyatı lazım.
3- get_pizza_area: pizzanın çapını kullanarak alanını hesaplayacak fonksiyon.
* ipucu: yarıçapın karesini pi ile çarpılır
* pi'yi 3.14 olarak alın
4- calculate_score: pizzanın alanı ve fiyatını kullanarak fiyat/performans hesaplayacak fonksiyon
* alan / fiyat

Bu noktadan sonra bir büyük bir de küçük pizza için kullanıcıdan input alcağız.
Sonrasında bu pizzaların alanlarını ve skorlarını hesaplayıp bunları ekrana yazdıracağız
En son da hangi pizza daha avantajlı ise o pizzayı kazanan olarak belirteceğiz.
"""

from math import pi


def get_input(text):
    user_input = input(text + ': ')
    if user_input.isdigit():
        return int(user_input)
    else:
        print('Lütfen bir sayı giriniz!!!!')
        return get_input(text)


def create_pizza(size):
    diameter = get_input(f'{size} pizza için çap')
    price = get_input(f'{size} pizza için fiyat')
    return {
        'diameter': diameter,
        'price': price,
    }


def get_pizza_area(diameter):
    r = diameter / 2
    area = pi * (r ** 2)
    return area


def calculate_score(pizza):
    area = get_pizza_area(pizza['diameter'])
    score = area / pizza['price']
    return score


def main():
    small_pizza = create_pizza('Küçük')
    large_pizza = create_pizza('Büyük')

    small_score = calculate_score(small_pizza)
    large_score = calculate_score(large_pizza)

    print(
        '\nVerimlilikler:\n    Küçük: {}\n    Büyük: {}\n'.format(
            round(small_score, 2), round(large_score, 2)
        )
    )

    if small_score > large_score:
        print('Küçük pizza daha verimlidir!')
    elif large_score > small_score:
        print('Büyük pizza daha verimlidir!')
    else:
        print('Pizzacınız takıntılı bir matematik mühendisidir!')


main()
