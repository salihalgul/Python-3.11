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

def is_prime(number):
  for j in range(2,number):
    if (number % j) == 0:
        return False
    j += 1
  return True


# for i in range(1, 51):
    # Burası da sizin fonksiyonu 1 ile 50 arasında çağıracağınız ve True dönerse ekrana yazdıracağınız yer olacak.

sonuc = []
for i in range(1, 51):
    if i == 1:
        continue
    bolen = 0
    for j in range(2, i):
        if (i % j == 0):
            bolen += 1
    if bolen == 0:
        sonuc.append(i)
print(f"Asal sayılar listesi = {sonuc}")
    



    



