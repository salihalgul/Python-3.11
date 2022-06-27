# Listeler, neredeyse her özelliği ile Tuple'lar ile aynıdır.
# Tek fark, Listeler sonradan modifiye edilebilir.

ornek_liste_1 = ['Nur', 'Salih', 'İrem', 'Kübra', 'Ömer', 'Fatih']

print(ornek_liste_1)
print(ornek_liste_1[2])


ornek_liste_1.append('Göktuğ')
print(ornek_liste_1)

# Pop komutu. Bu komut listeden indexini belirttiğimiz ögeyi çıkartıp bize veri olarak geri vverir.
son_utucu = ornek_liste_1.pop(6)

print(ornek_liste_1)
print(son_utucu)

# Remove komutu. Bu komut ise listeden spesifik olarak belirttiğimiz elemanı siler.
# Bu eleman direkt olarak ram'den silinir, bir daha bir işlem yapılmaz

ornek_liste_1.remove('Fatih')
print(ornek_liste_1)

kazanan = ornek_liste_1.remove('Kübra')
print(kazanan)
