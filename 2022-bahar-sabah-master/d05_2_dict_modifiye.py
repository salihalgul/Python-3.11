ornek_dict = {
    "name": "Yıldız",
    "surname": "Tilbe",
    "age": 55,
    "classroom": "Bakırköy 46",
}

ornek_dict['age'] = 56
print(ornek_dict)

ornek_dict.update({"gender": "Female"})

print(ornek_dict)

yeni_ornek_dict = {
    "name": "İbrahim",
    "surname": "Tatlıses",
    "surname": "Kutluay",
    "surname": "Deneme",
}

print(yeni_ornek_dict)

# keys metodu sözlüğümüzün anahtar kelimelerini bize bir liste olarak döner
dict_anahtarlari = ornek_dict.keys()
print(dict_anahtarlari)

# values metodu sözlüğümüzün değerlerini bize bir liste olarak döner
dict_valuelar = ornek_dict.values()
print(dict_valuelar)

# items metodu sözlüğümüzün hem anahtar hem de değerlerini tuple halinde paketleyerek bir liste olarak döndürür
dict_itemlar = ornek_dict.items()
print(dict_itemlar)
