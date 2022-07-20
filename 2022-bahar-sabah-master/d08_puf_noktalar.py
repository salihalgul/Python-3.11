ornek_virgullu_string = 'pazardan bir elma, armut,ananas, kavun, keçi al'

# Burada stringin sonundakı ' al' kısmını sildik
ornek_virgullu_string = ornek_virgullu_string.replace(' al', '')
# Burada da baştaki 'pazardan bir ' kısmını sildik
ornek_virgullu_string = ornek_virgullu_string.replace('pazardan bir ', '')

print(ornek_virgullu_string)

# Burada da kalan stringimizdeki boşlukları sildik
ornek_virgullu_string = ornek_virgullu_string.replace(' ', '')
# Burada da virgüller ile ayırarak stringimizin içeriğinden bir liste çıkarttık
stringden_listeye = ornek_virgullu_string.split(',')
print(stringden_listeye)

sayilacak_string = 'Ben bir ceviz ağacıyım gülhane parkında'
# Yeni stringimizin uzunluğunu ölçtük
print(len(sayilacak_string))
# Önceki listemizin uzunluğunu ölçtük
print(len(stringden_listeye))

# Burada count metodunu kullanarak string içerisindeki spesifik karakterleri saydık
print('a:', sayilacak_string.count('a'))
print('i:', sayilacak_string.count('i'))
print('Boşluk:', sayilacak_string.count(' '))
print('b:', sayilacak_string.count('b'))

# Print içerisinde virgül ile ayırdığımız elemanlar aralarında boşluk konularak ekrana yazdırılır
# Ayırma şeklini en sona 'sep' argümanını tanımlayarak değiştirebiliriz
print('elma', 'armut', 'mahmut', sep=' | ')

# join komutu ile bir listeyi string haline getirebiliriz.
# Bunun için ayraç olarak kullanacağımız ifadeyi bir string olarak tanımlayıp,
# join metodunun içerisine de birleştireceğimiz stringi veriyoruz
birlestirilecek_liste = ['Klaus', 'Hans', 'Thomas', 'Zübük']
birlestirilmis_string = ' % '.join(birlestirilecek_liste)
print(birlestirilmis_string)


taranacak_liste = ['Ahmet', 'Mehmet', 'Ali', 'Zübük', 'Mahmut', 'Kazım', 'Abdülmuttalip', 'Murtaza', 'Kamuran']

tarama_sonucu = []
for i in taranacak_liste:
    if i[0] == 'A':
        tarama_sonucu.append(i)

print(tarama_sonucu)


# unpacking konsepti bir liste ya da tuple'ın elemanlarının birden fazla değişken olarak kaydedilmesidir.

ornek_dagitilacak_tuple = ('Pacchi', 'Cengiz', 'Kont')

kedi, kus, kopek = ornek_dagitilacak_tuple
print(kus)
print(kopek)
print(kedi)

# bir stringe çarpma işlemi yaparsak eğer belirttiğimiz sayı kadar kendini tekrarlar
print('-' * 6)

# Unpacking esnasında listenin eleman sayısını bilmiyordak emin olduğumuz kadarını
# isimlendirip kalanları başına '*' koyduğumuz bir değişkene liste olarak atayabiliriz
bir, *kalan = ornek_dagitilacak_tuple

print(bir)
print(kalan)

print('-' * 6)

liste_icinde_liste = [
    ['ali', 12],
    ['veli', 23],
    ['hasan', 90],
    ['mahmut', 5, 5],
]

print(liste_icinde_liste[3][0])

for i in liste_icinde_liste:
    print(i[0], i[1], sep=' | ')

print('-' * 6)

# unpacking işlemini for içerisinde de yapabiliriz
# Aynı sıradaki elemanları belirttiğimiz değişken isimlerine atar
# Yıldız gene aynı işlemi yapmaktadır
for name, grade, *age in liste_icinde_liste:
    print(f'{name}: {grade}')
    # Boş bir liste if içerisinde direkt olarak False olarak algılanır
    if age:
        print(age)

sayilacak_liste = ['Pacchi', 'Pamuk', 'Mazlum', 'Ponpon']

# enumerate komutu kendisine verdiğimiz veri setini bir index numarası ile
# tuple içerisine alıp geri döndürür.
# tuple'ın ilk elemanı index, ikinci elemanı ise objemizdir
sayilmis_liste = enumerate(sayilacak_liste)
print(list(sayilmis_liste))

for index, value in enumerate(sayilacak_liste):
    print(f'{index}: {value}')

print('-' * 6)

# Aynı işlemi dict objelerinin items metoduna da yapabiliriz
# Çünkü verdikleri çıktı liste içerisinde liste şeklindedir.
ornek_dict = {'name': 'Pacchi', 'gender': 'Female', 'type': 'Cat', 'age': 2}

print(list(ornek_dict.items()))

for key, value in ornek_dict.items():
    print(f'{key}: {value}')
