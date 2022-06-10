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

email = "salihalgul@gmail.com"
password = "abc123"

girilenemail = input("email:")
girilenpassword = input("password:")

if (girilenemail == email):
    if (girilenpassword == password):
        print("Uygulamaya giriş başarılı.")
    else:
        print("Uygulamaya parolanız hatalı")
else:
    print("Uygulamaya giriş email bilginiz hatalı.")
