def ornek_fonksiyon(arg1, arg2, arg3):
    print('arg1', type(arg1), arg1)
    print('arg2', type(arg2), arg2)
    print('arg3', type(arg3), arg3)


# fonksiyona istediği miktarda argümanı vermek zorundasınız.
# Ama bu zorunluluk sadece pozisyon, yani index tabanlı argümanlar için geçerlidir
ornek_fonksiyon('ali', 12, 40.2)
# ornek_fonksiyon('ali', 12, 40.2, 'Çekoslovakyalılaştıramadıklarımız')
# ornek_fonksiyon('ali', 12)


# * ile bir argümanın birden fazla argüman şeklinde olmasını sağlayabiliriz.
# kendisine vereceğimiz fazladan argümanlar fonksiyon içerisinde bir tuple haline gelir
def arguman_grubu(arg1, *args):
    print(args)


arguman_grubu('ali', 'veli', 'mahmut')
arguman_grubu(12, 'asdkjghadskjgj', False)


# Keyword argümanlar, tıpkı dict objeleri gibi index yerine bir anahtar kelime ile tanımlanır
# Bunlar fonskiyon çağırılırken bu isim kullanılarak tanımlanır.
# Keyword argümanlar pozisyonlu argümanların aksine default değer alabilirler

print('-' * 20)


def ornek_keyword_fonkskiyon(name='Mahmut', surname='Tuncer'):
    print(f'Bu kişinin adı "{name}" soyadı "{surname}"')


ornek_keyword_fonkskiyon(name='Ali', surname='Ağaoğlu')
ornek_keyword_fonkskiyon(surname='Tilbe', name='Yıldız')
ornek_keyword_fonkskiyon()

print('-' * 20)


def bir_baska_keyword_ornek(arg1=None, arg2=None):
    if arg1 and arg2:
        print('İki argüman da tanımlı')
    elif arg1:
        print('Sadece arg1 tanımlı')
    elif arg2:
        print('Sadece arg2 tanımlı')
    else:
        print('Hiçbir arg tanımlı değil')


bir_baska_keyword_ornek(arg1=12, arg2=12)
bir_baska_keyword_ornek(arg2=12)
bir_baska_keyword_ornek(arg1=12)
bir_baska_keyword_ornek()


def karisik_argli_fonksiyon(arg1, arg2, kwarg1=None, kwarg2=None):
    print(arg1, arg2, kwarg1, kwarg2)


print('-' * 20)


def ornek_packed_kwargs(**kwargs):
    print(kwargs)


ornek_packed_kwargs(name='ali', surname='veli', age=2)
ornek_packed_kwargs(price=55, radius=26)
