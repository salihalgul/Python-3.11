from random import choice


mahmut = {
    'name': "Mahmut",
    'surname': 'Tuncer',
    'age': 'As long as a halay',
    'job': 'halaybaşı',
    'title': 'LO',
}


def reverse_string(string):
    """
    Bu fonskiyon kendisine verdiğimiz herhangi bir stringi tersine çevirir.
    """
    return string[::-1]


def greet_me(name):
    """
    Bu fonksiyonda verdiğimiz bir ismi alıp başına rastgele bir selamlama şekli ekler.
    """
    greet_list = (
        'Hello there',
        'Merhabalar',
        'Konnichiha',
        'Sup mate',
    )

    # `random` kütüphanesinden `choice` fonksiyonu, kendisine verilmiş bir
    # veri grubundan rastgele bir eleman seçip geri verir.
    rand_greet = choice(greet_list)

    return f'{rand_greet} {name}'
