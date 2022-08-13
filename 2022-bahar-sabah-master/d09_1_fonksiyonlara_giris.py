def ornek_fonksiyon_bir():
    print('Burasi fonksiyonun baslangic noktasidir')
    b = 2 + 3
    print(b)
    print('Burasi da fonksiyonun bitis noktasidir')


print('Burasi ise fonskiyonun disindadir')

ornek_fonksiyon_bir()
ornek_fonksiyon_bir()


print('-' * 10)


def ciktili_ornek_fonksiyon():
    b = 20 * 10
    return b


ornek_cikti = ciktili_ornek_fonksiyon()

print(ornek_cikti * 10)

print(ciktili_ornek_fonksiyon() / 15)
print(type(ciktili_ornek_fonksiyon()))
print(type(ciktili_ornek_fonksiyon))
print(type(ornek_fonksiyon_bir()))


def argumanli_fonksiyon(mahmut):
    if type(mahmut) == str:
        return mahmut[::-1]
    elif type(mahmut) == int:
        return mahmut / 12

cikti = argumanli_fonksiyon('mahmut')
print(cikti)
print(type(cikti))

print(
    argumanli_fonksiyon('Ali Ata Bak')
)
print(
    argumanli_fonksiyon(42)
)
print(
    argumanli_fonksiyon(['Ali', 'Veli'])
)


def karesini_alip_bol(sayi, bolen):
    print('Sayi:', sayi)
    print('Bolen:', bolen)

    karesi = sayi * sayi
    bolum = karesi / bolen
    return bolum


cikti = karesini_alip_bol(12, 8)

print(cikti)
