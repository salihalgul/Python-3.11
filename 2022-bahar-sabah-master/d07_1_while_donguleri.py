"""
Döngüler, programımız içerisinde kendini bir koşula göre sürekli tekrarlayan kod parçalarıdır.
Python içerisinde iki farklı tip döngümüz vardır.
Bunlardan ilki "while" döngüleridir.
While döngüleri kendisine belirttiğimiz bir boolean işlemi True olduğu süre içerisinde tekrarlar.
"""

i = 0

while i <= 10:
    print(i)
    i += 2

"""
Eğer aşağıdaki gibi yapsaydık "i" hiçbir zaman 10'dan büyük olmayacağı için
bu döngü sonsuza dek tekrarlayacaktı.

i = 0

while i <= 10:
    print(i)
"""

print('\nYENI\n')
j = 35

while True:
    if j % 20 == 0:
        break
    print(j % 20)
    j += 1

"""
break komutu çalıştığı anda içerisinde bulunduğu döngüyü tamamen bozar.
Döngünün koşulu ya da kalan turları neyse hepsi çöpe atılır ve umursanmaz.

Ek olarak yukarıdaki örnek şu şekilde de yazılabilirdi, sadece break örneği olsun diye böyle yazıldı.

j = 35

while j % 20 != 0:
    print(j % 20)
    j += 1
"""
