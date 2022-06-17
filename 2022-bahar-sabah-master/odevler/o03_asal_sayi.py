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

number = "1"
is_prime = False

def is_prime(number):
    if (number == 1):
        return False
    elif ( number == 2):
        return True
    else:
        for i in range(2, number + 1):
            if (number % i == 0):
                return False
            else:
                return True
 


# for i in range(1, 51):
    # Burası da sizin fonksiyonu 1 ile 50 arasında çağıracağınız ve True dönerse ekrana yazdıracağınız yer olacak.

is_prime = []
for i in range(1, 51):
    if i == 1:
        continue
    bolen = 0
    for j in range(2, i):
        if (i % j == 0):
            bolen += 1
    if bolen == 0:
        is_prime.append(i)
print(f"Asal sayılar listesi = {is_prime}")
    



    



