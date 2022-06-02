"""
FizzBuzz temel bir programlama egzersizidir.
Hem yeni başlayan/yeni bir dil öğrenen programcılar için,
hem de yeni oluşan bir dilin temel özelliklere sahip olup olmadığını
anlamak için kullanılır.

FizzBuzz'ın çalışma şekli:
- iki sayı arasında bir döngü kurulur.
- Eğer o turdaki sayı 3'e bölünebiliyorsa ekrana "Fizz"
- Sayı 5'e bölünebiliyorsa ekrana "Buzz"
- Sayı hem 3'e hem de 5'e bölünebiliyorsa ekrana "FizzBuzz"
- Hiçbirine bölünemiyorsa da ekrana sayının kendisi yazılır.
"""

for i in range(1, 51):
    # if i % 15 == 0:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

*x,y,z=(4, 8, 15, 16, 23, 42)
print(x,y,z) 
