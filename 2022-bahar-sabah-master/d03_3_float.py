# Float yani küsüratlı sayılar
# integer gibi direkt olarak sayının yazılması ile tanımlanır

ornek_float = 10.9
print(ornek_float)

print(ornek_float + 10)
print(ornek_float - 10)
print(ornek_float * 10)
print(ornek_float / 10)

ornek_bozuk = 0.1 + 0.2
print(ornek_bozuk)

ornek_duzeltme_1 = round(ornek_bozuk)
print(ornek_duzeltme_1)

ornek_duzeltme_2 = round(0.342173, 3)
print(ornek_duzeltme_2)

ornek_buyuk = 124787345
print(round(ornek_buyuk, -6))
