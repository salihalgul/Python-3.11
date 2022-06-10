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

sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]


sesli_sayim = {i : str.count(i) for i in sesli}
print(sesli_sayim)


mod_str = str.lower().strip()

for i in sesli:
    print(f"{i} = {mod_str.count(i)}")


