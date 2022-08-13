"""
Tuple birden fazla veriyi sırasıyla bir grup halinde tutmanızı sağlar.
Tuple'dan ögeler sırası yani "index" verisi kullanılarak çekilebilir.
İndex, Python içerisinde 0'dan başlar.
Tuple'lar aynı veriyi birden fazla kere barındırabilir.
Tuple'lar immutable yani sonradan değiştirilemez verilerdir.
"""

ornek_tuple_1 = ('Ali', 'Veli', 'Hasan', 42)
ornek_tuple_2 = 'Mahmut', 'Yıldız', 'İbrahim', 99

print(ornek_tuple_1)
print(ornek_tuple_2)

ornek_tuple_2 = ('Murtaza', 'Şuaip', 'Eyşan', 'Ahmet')
print(ornek_tuple_2)

# Tuple içerisinden index kullanarak bir veri çekmek için "[index_numarası]" kullanılır
ornek_veri_1 = ornek_tuple_1[0]
print(ornek_veri_1)

# Bir aralık vermesini istiyorsak : ile ayırarak iki indeximizi belirtiyoruz
print(ornek_tuple_2[1:3])

print(ornek_tuple_2[:3])
print(ornek_tuple_2[2:])

print(ornek_tuple_2[::-1])

print(ornek_tuple_2[-1])
# Eğer indexten fazla bir sayı girersek Python burada bize IndexError hatası verecektir
# print(ornek_tuple_2[6])
