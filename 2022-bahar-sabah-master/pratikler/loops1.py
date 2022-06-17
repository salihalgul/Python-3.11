"""
1-100 arasında rasgele üretilecek olan bir sayıyı aşağı ve yukarı ifadeleri ile buldurmaya çalışın.
** "random modülü" için "python random" şeklinde arama yapın.
** 100 üzerinden puanlama yapın. Her soru 20 puan (hak = 5)
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

import random

sayi = random.randint(1,100)

can = int(input('Kaç hak kullanmak istersiniz? : '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin : '))

    if (sayi == tahmin):
        print(f'Tebrikler sayıyı {sayac}. defada bildiniz. Toplam puanınız {100 - ((100/can) * (sayac - 1))} ')
        break
    elif sayi > tahmin:
        print('Yukarı')
    else:
        print('Aşağı')
    if hak == 0:
        print(f'Hakkınız bitti. Tutulan sayı : {tahmin}')
