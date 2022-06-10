# isim = input("isminiz: ")
# yas = float(input("yaşınız: "))
# egitim = input("eğitiminiz: ").lower().strip()
# if (yas>=18): 
#     if (egitim=="lise" or egitim=="üniversite"):
#         print(f"{isim} ehliyet alabilirsin.")
#     else:
#         print(f"{isim} ehliyet alamazsın eğitim durumun yetersiz")
# else:
#     print(f"{isim} ehliyet alamazsın yaşınız tutmuyor")

# yazili1 = float(input("1. yazılı: "))
# yazili2 = float(input("2. yazılı: "))
# sozlu = float(input("sozlu: "))
# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if (ortalama>=0) and (ortalama<25):
#     print(f"ortalamanız: {ortalama} notunuz: 0")
# elif (ortalama>=25) and (ortalama<45):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif (ortalama>=45) and (ortalama<55):
#     print(f"ortalamanız: {ortalama} notunuz: 2")
# elif (ortalama>=55) and (ortalama<70):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif (ortalama>=70) and (ortalama<85):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif (ortalama>=85) and (ortalama<=100):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# else:
#     print("yanlış bilgi girdiniz")

import datetime


tarih = input("Aracınız hangi tarihte trafiğe çıktı?(YYYY/AA/GG): ")                        
tarih = tarih.split("/")
simdi = datetime.datetime.now()

trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark = simdi - trafigecikis
days = fark.days

if (days<=365):
    print("1. servis aralığı")      
elif (days>365) and (days<=365*2):
    print("2. servis aralığı")
elif (days>365*2) and (days<=365*3):
    print("3. servis aralığı")
else:
    print("hatalı süre.")