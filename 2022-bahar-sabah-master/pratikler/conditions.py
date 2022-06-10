# Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# sayı = float(input("bir sayı giriniz: "))

# if (sayı>0) and (sayı<=100):
#     print("Sayı 0-100 arasındadır.")
# else:
#     print("Sayı 0-100 arasında değildir.")

# Girilen bir sayının pozitif çift sayı olup olmadığını denetleyiniz.

# sayi = int(input("Bir sayı giriniz: "))

# if (sayi>0):
#     if (sayi % 2 == 0):
#         print(f"Girilen {sayi} sayısı pozitif çift sayıdır.")
#     else:
#         print(f"Girilen {sayi} sayısı pozitif ama tektir.")
# else:
#     print(f"Girilen {sayi} sayısı negatifdir.")

# Email ve parola bilgileri ile giriş kontrolü yapınız

# email = "salihalgul@gmail.com"
# password = "abc123"

# girilenemail = input("email: ")
# girilenpassword = input("password: ")

# if (girilenemail == email):
#     if (girilenpassword == password):
#         print("Uygulamaya giriş başarılı.")
#     else:
#         print("Uygulamaya parolanız hatalı")
# else:
#     print("Uygulamaya giriş email bilginiz hatalı.")

# Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# b = float(input("b: "))
# c = float(input("c: "))
# a = float(input("a: "))   

# if (a>b) and (a>c):
#     print(f"a: {a} en büyük sayıdır.")
# elif (b>a) and (b>c):
#     print(f"b: {b} en büyük sayıdır.")
# elif (c>a) and (c>b):
#     print(f"c: {c} en büyük sayıdır.")

# Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
# a) Ortalama 50 olsa bile final notu en az 50 olmalıdır.
# b) Finalden 70 alındığında ortalamanın önemi olmasın.

# vize1 = float(input("vize1: "))
# vize2 = float(input("vize2: "))
# final = float(input("final: "))

# ortalama = ((vize1 + vize2) / 2 * 0.6) + (final * 0.4)

# if (ortalama >= 50) and (final >= 50):
#     print(f"{ortalama} ile geçtiniz." )
# elif (final >= 70):
#     print(f"{ortalama} ile ortalamaya bakılmaksızın geçtiniz.")
# elif (final < 50):
#     print("Final notunuz 50 nin altında olduğu için kaldınız.")
# else:
#     print(f"{ortalama} ile kaldınız. Üzgünüm!")

"""Kişinin ad, kilo, boy bilgilerini alıp kilo indekslerini hesaplayınız.
Formül: (kilo / boy uzunluğunun karesi)
Aşağıdaki tabloya göre kişi hangi gruba girmektedir bakınız.
0-18.4 => Zayıf
18.5-24.9 => Normal
25.0-29.9 => Fazla Kilolu
30.0-34.9 => Şişman (Obez) """

name = input("adınız: ")
kg = float(input("kilonuz: "))
hg = float(input("boyunuz: "))

index = kg / (hg ** 2)


if (index>=0) and (index<=18.4):
    print(f"{name} kilo index'in {index} ve kilo değerlendirmen: Zayif")
elif (index>18.4) and (index<=24.9):
    print(f"{name} kilo index'in {index} ve kilo değerlendirmen: Normal")
elif (index>24.9) and (index<=29.9):
    print(f"{name} kilo index'in {index} ve kilo değerlendirmen: Fazla Kilolu")
elif (index>29.9) and (index<=34.9):
    print(f"{name} kilo index'in {index} ve kilo değerlendirmen: Obez")
else:
    print("Sen neymişsin be abi ! A! A! A!")
