"""
Bu ödev için bir sayının asal olup olmadığını denetleyen bir fonksiyon yazacaksınız.
Eğer sayı asal ise fonksiyon True, değilse False dönecek.
Fonksiyon argüman olarak sadece sayıyı alacak.

Sonrasında da bu fonksiyonu 1-50 arası bir döngüdeki bütün sayılar ile test edecek bir döngü yazılacak.
Fonksiyon True dönerse bu sayı ekrana yazdırılacak.

Size aşağıda Fonksiyon ve döngü için bir kalıp verildi. O kalıbın içerisinde kodunuzu yazınız.
"""


def is_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


for i in range(1, 51):
    if is_prime(i):
        print(i)
