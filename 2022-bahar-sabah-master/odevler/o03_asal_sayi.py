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

def is_prime(number, array):
    if array[0] == number:
        return True
    else:
        step = array[0]
        for i in range(len(array) - 1, 0, -1):
            if array[i] % step == 0:
                del array[i]
    if number not in array:
        return False
    return is_prime(number, array[1:])

# for i in range(1, 51):
    # Burası da sizin fonksiyonu 1 ile 50 arasında çağıracağınız ve True dönerse ekrana yazdıracağınız yer olacak.

sonuc = []
for i in range(1, 51):
    bolen = 0
    for j in range(2, i):
        if (i%j == 0):
            bolen += 1
    if bolen == 0:
        sonuc.append(i)
print(f"Asal sayılar listesi = {sonuc}")
    



    



