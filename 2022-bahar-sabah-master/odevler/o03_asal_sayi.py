"""
Bu ödev için bir sayının asal olup olmadığını denetleyen bir fonksiyon yazacaksınız.
Eğer sayı asal ise fonksiyon True, değilse False dönecek.
Fonksiyon argüman olarak sadece sayıyı alacak.

Sonrasında da bu fonksiyonu 1-50 arası bir döngüdeki bütün sayılar ile test edecek bir döngü yazılacak.
Fonksiyon True dönerse bu sayı ekrana yazdırılacak.

Size aşağıda Fonksiyon ve döngü için bir kalıp verildi. O kalıbın içerisinde kodunuzu yazınız.
"""



# def is_prime(number):
    # Bu sizin asal sayı kontrol edecek fonksiyonunuz olacak


def is_Prime(num1, num2):
    for Mahmut in range(num1, num2+1):
        if Mahmut > 0:
            for i in range(2, Mahmut):
                if (Mahmut % i == 0):
                    print(f'{Mahmut} : False means Non-Prime')
                    break
            else:
                print(f'{Mahmut} : True means Prime(Yesss yess yesss !!! i found you !!!)')

num1 = int(input('Nereden başlayalım ? : '))
num2 = int(input('Nerede bitsin ? : '))

is_Prime(num1, num2)
    

# for i in range(1, 51):
    # Burası da sizin fonksiyonu 1 ile 50 arasında çağıracağınız ve True dönerse ekrana yazdıracağınız yer olacak.
