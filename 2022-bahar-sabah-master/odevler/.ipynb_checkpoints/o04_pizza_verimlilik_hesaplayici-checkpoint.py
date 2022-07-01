"""
Bu programımız kullanıcıdan aldığı inputlar ile oluşturduğu iki pizzayı birbiri ile
kıyaslayıp fiyat/performans olarak hangisinin daha verimli olduğunu belirleyecek.

Bu program içerisinde sizden birkaç tane fonksiyon yazmanızı isteyeceğim.
1- get_input: Kullanıcıdan input alıp bunu işleyecek fonksiyon.
2- create_pizza: Kullanıcıdan aldığı input ile pizza oluşturacak fonksiyon.
* Pizza içeriği olarak sadece çapı ve fiyatı lazım.
3- get_pizza_area: pizzanın çapını kullanarak alanını hesaplayacak fonksiyon.
* ipucu: yarıçapın karesini pi ile çarpılır
* pi'yi 3.14 olarak alın
4- calculate_score: pizzanın alanı ve fiyatını kullanarak fiyat/performans hesaplayacak fonksiyon
* alan / fiyat

Bu noktadan sonra bir büyük bir de küçük pizza için kullanıcıdan input alcağız.
Sonrasında bu pizzaların alanlarını ve skorlarını hesaplayıp bunları ekrana yazdıracağız
En son da hangi pizza daha avantajlı ise o pizzayı kazanan olarak belirteceğiz.
"""

pi = 3.14

def kucuk_pizza_performans():
           
    pizza_fiyati = int(input("Lütfen küçük pizza fiyatı giriniz: "))
    
    pizza_capi = int(input("Lütfen küçük pizza çapını giriniz: "))

    pizza_alani = pi * (pizza_capi/2)**2
    
    performans = pizza_fiyati / pizza_alani
    
    return performans


print("Küçük pizza performans puanı :", kucuk_pizza_performans())
    
def buyuk_pizza_performans():
           
    buyuk_pizza_fiyati = int(input("Lütfen büyük pizza fiyatı giriniz: "))
    
    buyuk_pizza_capi = int(input("Lütfen büyük pizza çapını giriniz: "))

    buyuk_pizza_alani = pi * (buyuk_pizza_capi/2)**2
    
    buyuk_performans = buyuk_pizza_fiyati / buyuk_pizza_alani
    
    return buyuk_performans


print("Büyük pizza performans puanı :", buyuk_pizza_performans())

if buyuk_pizza_performans() > kucuk_pizza_performans():
    print("Şampiyon Büyük Pizza")
else:
    print("Şampiyon Küçük Pizza")