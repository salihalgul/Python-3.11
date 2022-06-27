"""
Sözlükler yani dict veriyi anahtar kelime ve değer şeklinde tutar.
Veriye erişmek için anahtar kelimeyi kullanırız.
Dict ögeleri sonradan modifiye edilebilirler
"""

ornek_dict_1 = {
    "name": "Mahmut",
    "surname": "Tuncer",
    "age": 68
}

print(ornek_dict_1)

print(ornek_dict_1["surname"])
# Olmayan bir anahtari [] ile çağırırsak bu bize KeyError verecektir
# print(ornek_dict_1["gender"])

# Var olmama olasılığı olan bir veride get komutunu kullanabiliriz. Bize olmadığı durumda None döner
print(ornek_dict_1.get("gender"))

print(ornek_dict_1.get("class", "C301"))
print(ornek_dict_1.get("name", "Abdulrezzak"))
