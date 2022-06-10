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

# sesli = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
# sesli_sayim = {i : str.count(i) for i in sesli}

sesli_sayim = {i : str.count(i) for i in 'aeıioöuü'}
sertsessiz_sayim = {mahmut : str.count(mahmut) for mahmut in 'çfthskpş'}

print(sesli_sayim)

mod_str = str.lower().strip()

# for i in sesli:
for i in 'aeıioöuü':
    print(f"{i} = {mod_str.count(i)}")

print(f"Sert sessizler sözlüğü= {sertsessiz_sayim}")
for mahmut in 'çfthskpş':
    print(f"Sert sessiz {mahmut} harfi {mod_str.count(mahmut)} adettir.")

