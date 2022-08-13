"""
Python altında dosya okumak için `open` komutu kullanılır.
Bu komut sizin belirttiğiniz yöntem ile dosyayı açar ve
üzerinde işlem yapmanızı sağlar.

Özellikle kullanacağınız dosya okuma yöntemleri:
- `r` = Read, yani okuma modu. Burada sadece dosyayı okur. Default moddur
- `w` = Write, dosyaya yazma işlemi yapar.
    Ama dosyanın bütün içeriğini birlikte değiştirir
- `a` = Append, dosyanın önceki içeriğini silmeden sadece sonuna ekleme yapar
- `x` = Sıfırdan dosya yaratır. `w` ve `a` işlemleri de bunu yapar.
    Ama bazen hiçbir şey yazmadan dosya oluşturmamız da gerekir.
"""

ornek_dosya_1 = open("hello.py", "r")

print(type(ornek_dosya_1))
print(ornek_dosya_1)
ornek_dosya_lines = ornek_dosya_1.readlines()
print(type(ornek_dosya_lines))

for i in ornek_dosya_lines:
    print(i)

print("bu noktada ben artik dosya ile calismiyorum")
print("ama dosya hala ramde")
print("Hele Windows altindaysaniz eger, program kapanmadan dosya erisilemez")
print(ornek_dosya_1)

ornek_dosya_1.close()


"""
with komutu ile açma ve kapama işlemi olan herhangi bir fonksiyonu
kapatma kısmını belirtmenize gerek kalmadan kullanabilirsiniz.
`open` komutu dışında veritabanı bağlantıları gibi işlemler de with ile kullanılır
"""

with open("hello.py", "r") as file:
    print("yeni okumamiz burada basliyor", file)
    print(file.read())

print('Bu noktada dosyamiz artik ramde degildir.')
