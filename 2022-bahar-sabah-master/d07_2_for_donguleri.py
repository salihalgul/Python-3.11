"""
For döngüleri kendi içerisine verdiğimiz bir veri setini dönrürür.
Her turda veri setinin bir sonraki elemanını belirttiğimiz değişken adı
ile kaydederek turu çalıştırır. Sonraki tur da bir sonraki set elemanı
aynı değişken adı ile kullanılır.

for {geçici_değişkenin_adı} in {veri_setimiz}:
    {çalıştıracağımız komutlar}
"""

ogrenciler = ['Fatih', 'Salih', 'Ömer']

for mahmut in ogrenciler:
    print(mahmut)
    print('********')


ornek_sira = range(1, 6)
print(list(ornek_sira))

for sayi in range(1, 11):
    if sayi % 3 == 0:
        print('Atlayalim mi abi?')
        continue
        print('Atlayalim be ya!')
    print(sayi)

print('Bu da döngü bitince yazılacak')
"""
continue komutu döngü içerisinde çalışırsa eğer o turu komple atlayıp bir sonraki tura geçecektir.
NOT: break ve continue komutları hem for hem de while döngüleri içerisinde kullanılabilir.
"""
