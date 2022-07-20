# String: Python içerisideki düz metin yani yazı içeriklerdir.
# Python içerisinde stringler tek tırnak ' ya da çift tırnak " arasında yazılarak tanımlanır

ornek_string = "Bu bir stringdir"

# upper komutu stringin tamamen büyük harflere dönüşmesini sağlar
print(ornek_string.upper())

# lower komutu strngin tamamen küçük harflere dönüşmesini sağlar
print(ornek_string.lower())

# [::-1] diyerek stringimizi ters çevirebiliriz
print(ornek_string[::-1])

# capitalize komutu stringimizin sadece baş harfini büyük hale getirir.
print("bir baska deneme".capitalize())

hello = 'Merhaba gençler'
# Artı işareti ile iki stringi birbiriyle birleştirebiliyoruz.
hello2 = hello + ', ve daima genç kalanlar!'

print(hello)
print(hello2)

# hello = hello + ', ve daima genc kalanlar!'
hello += ', ve daima genç kalanlar!'
print(hello)
print(hello2)

ornek_format = '{} ile {} bakkala gitti. ve {{}} seklinde sticker aldı.'.format("Ali", "Veli")
print(ornek_format)

a = "Mahmut"
b = "İbrahim"

ornek_format_2 = f"{a} ile {b} show tvye çıktı"
print(ornek_format_2)
