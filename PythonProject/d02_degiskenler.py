# Değişkenler, programımızda bir veriyi bir anahtar kelime aracılığı ile 
# sonradan çağırılabilecek şekilde sakladığımız araçlardır.
hello = "Hello World"
print(hello)

hello = "Konnichiha Sekai"
print(hello)


def ornek_fonksiyon():
    fonksiyon_ici_degisken = "Mahmut"
    print(fonksiyon_ici_degisken)
    hello = "Merhaba Dunya"
    print(hello)


print(hello)
# print(fonksiyon_ici_degisken)
ornek_fonksiyon()
