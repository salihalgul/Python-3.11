kucuk_pizza_fiyati = int(input("Lütfen küçük pizza fiyatı giriniz(TL): "))
    
kucuk_pizza_capi = int(input("Lütfen küçük pizza çapını giriniz(cm): "))
    
buyuk_pizza_fiyati = int(input("Lütfen büyük pizza fiyatı giriniz(TL): "))
    
buyuk_pizza_capi = int(input("Lütfen büyük pizza çapını giriniz(cm): "))

pi = 3.14

kucuk_performans = 0

buyuk_performans = 0

def pizza_verimlilik():
        
    kucuk_pizza_alani = pi * (kucuk_pizza_capi / 2)**2
    
    kucuk_performans = kucuk_pizza_alani / kucuk_pizza_fiyati
    
    buyuk_pizza_alani = pi * (buyuk_pizza_capi / 2)**2
    
    buyuk_performans = buyuk_pizza_alani / buyuk_pizza_fiyati

    kucuk = round(kucuk_performans, 2)
    buyuk = round(buyuk_performans, 2)

        
    if kucuk > buyuk:
        
        print(f"Küçük pizza % {kucuk} performans ile daha başarılıdır.")
        print(f"Büyük pizza performansı % {buyuk} de kalmıştır.")
        
    else:
        
        print(f"Büyük pizza % {buyuk} performans ile daha başarılıdır.")
        print(f"Küçük pizza performansı % {kucuk} de kalmıştır.")
        
pizza_verimlilik()