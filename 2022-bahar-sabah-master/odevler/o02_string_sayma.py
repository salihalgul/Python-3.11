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

string_to_count = """
Başım köpük köpük bulut
İçim dışım deniz
Ben bir ceviz ağacıyım Gülhane Parkı’nda
Budak budak, şerham şerham ihtiyar bir ceviz
Ne sen bunun farkındasın ne polis farkında

Ben bir ceviz ağacıyım Gülhane Parkı’nda
Ne sen bunun farkındasın ne de polis farkında
"""


def sayma(metin, sayilacak):
    lower_string = metin.lower()
    count_dict = {}

    for i in sayilacak:
        count_dict.update(
            {
                i: lower_string.count(i)
            }
        )

    return count_dict


sayilmis = sayma(string_to_count, 'aeıioöuü')

for key, value in sayilmis.items():
    print(f'{key} = {value}')

