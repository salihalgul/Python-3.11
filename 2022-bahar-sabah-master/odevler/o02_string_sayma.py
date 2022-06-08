"""
Bu ödevde size verilecek bir string içerisindeki sesli harfleri sayıp bunları bir dict olarak kaydedeceksiniz.
dict objeniz aşağıdaki gibi olacaktır:
{
    'a': 7,
    'e': 9,
    'i': 4,
    ........
}

Sonrasinda bu dict objesini aşağıdaki formatta ekrana yazdıracaksınız:

a = 7
-----
e = 9
-----
i = 4
-----
..........


Örnek stringiniz de:
Başım köpük köpük bulut
İçim dışım deniz
Ben bir ceviz ağacıyım Gülhane Parkı’nda
Budak budak, şerham şerham ihtiyar bir ceviz
Ne sen bunun farkındasın ne polis farkında

Ben bir ceviz ağacıyım Gülhane Parkı’nda
Ne sen bunun farkındasın ne de polis farkında
"""
str = "Başım köpük köpük bulut İçim dışım deniz Ben bir ceviz ağacıyım Gülhane Parkı’nda Budak budak,şerham şerham ihtiyar bir ceviz Ne sen bunun farkındasın ne polis farkında Ben bir ceviz ağacıyım Gülhane Parkı’nda Ne sen bunun farkındasın ne de polis farkında"
sesli = ["A", "a", "E", "e", "I", "ı", "İ", "i", "O", "o", "Ö", "ö", "U", "u", "Ü", "ü"]
# result = str.split(" ")
i = 0
sesli_adedi = ["A: "]
for i in sesli:
    sesli_adedi = input("Sesli:")
    print(str.count(i))