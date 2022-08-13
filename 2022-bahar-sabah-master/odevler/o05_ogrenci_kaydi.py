"""
Bu projede 3 tane classımız olacak
Öğrenci, Öğretmen, Sınıf

Sınıf içeriği:
    * Öğrenciler: Öğrenci objesini liste olarak alacak.
    * Öğretmen: Öğretmen objesi direkt olacak
    * Konu
    * Sınıf oda numarası

    * Öğrenci ekleme
    * Öğretmen değiştirme
    * Öğrenci ve not ortalamalarını listeleme
"""
class Kategori:
    pass
    def __init__(self, konusu, ad, soyad, dogum_tarihi, yas, cinsiyet, notlar, not_ortalamasi, uzmanlik, oda_numarasi):
        self.konu = konu
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.notlar = notlar
        self.not_ortalamasi = not_ortalamasi
        self.uzmanlik = uzmanlik
        self.oda_numarasi = oda_numarasi
        

class Sinif:
    pass
    def __init__(self, konusu, oda_numarasi):
        self.konusu = konusu
        self.oda_numarasi = oda_numarasi        

class Ogretmen:
    pass
    def __init__(self, ad, soyad, dogum_tarihi, yas, cinsiyet, notlar, not_ortalamasi, uzmanlik, oda_numarasi):
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.notlar = notlar
        self.not_ortalamasi = not_ortalamasi
        self.uzmanlik = uzmanlik
        self.oda_numarasi = oda_numarasi


class Ogrenci:
    pass
    def __init__(self, ad, soyad, dogum_tarihi, yas, cinsiyet, notlar, not_ortalamasi, uzmanlik, oda_numarasi):
        self.ad = ad
        self.soyad = soyad
        self.dogum_tarihi = dogum_tarihi
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.notlar = notlar
        self.not_ortalamasi = not_ortalamasi
        self.uzmanlik = uzmanlik
        self.oda_numarasi = oda_numarasi
       

    # class attributes
    
    # consructor (yapıcı metod)
    
    # object attributes
    
    # methods

# object (instance)

sinif = Sinif(konusu, oda_numarasi)
ogrenci = Kategori(ad, soyad, dogum_tarihi, cinsiyet, notlar, yas, not_ortalamasi, gecer_mi)
ogretmen = Kategori(ad, soyad, dogum_tarihi, cinsiyet, uzmanlik, yas)


print(f'Sınıf konu: {sinif.konusu} oda numarası: {sinif.oda_numarasi}')
print(f'Öğrenci ad: {ogrenci.ad} soyad: {ogrenci.soyad} dogum tarihi: {ogrenci.dogum_tarihi} yas: {ogrenci.yas} cinsiyet: {ogrenci.cinsiyet} notlar: {ogrenci.notlar} not ortalamasi: {ogrenci.not_ortalamasi} gecer mi: {ogrenci.gecer_mi}')
print(f'Öğretmen ad: {ogretmen.ad} soyad: {ogretmen.soyad} dogum tarihi: {ogretmen.dogum_tarihi} yas: {ogretmen.yas} cinsiyet: {ogretmen.cinsiyet} uzmanlik: {ogretmen.uzmanlik} oda numarasi: {ogretmen.oda_numarasi}')






"""
Öğrenci içeriği:
    * ad-soyad
    * yaş
    * cinsiyet
    * notlar

    * Not ekleme
    * yaşlandırma
    * Not ortalaması alma
    * Geçme durumunu kontrol etme

Öğretmen içeriği:
    * ad-soyad
    * yaş
    * cinsiyet
    * uzmanlık alanları

    * uzmanlık alanı ekleme
    * yaşlandırma
"""
