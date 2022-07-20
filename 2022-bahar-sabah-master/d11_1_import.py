"""
Bir program yazarken ihtiyacımız olan her şeyi tek bir dosyada
yazmaya kalkışırsak eğer, bu bize büyük bir külfet yataracaktır.

Bunun yerine pek çok işlem farklı dosyalar içerisinde yazılıp,
kullanacağımız yerde çağırılabilir.

Bu çağırma işlemini Python projemizin görebildiği bir yolda
bulunan herhangi bir dosyadan yapabiliriz.

Bu yollar:
    - Python projemizin bulunduğu dizin ve alt dizinleri
    - Python'ın standart kütüphaneleri, yani her Python sisteminde olan kütüphaneler
        Python standart kütüphaneleri: https://docs.python.org/3/library/index.html
    - Python projemize bağlı sanal ortam (ileride gösterilecek)
    - Sistemimizde ya da sanal ortamımızda kurulu ek kütüphaneler

Şu an için sadece ilk iki kısım gösterilecek.

Bu dersimizde ilk grup için bu projemizin altında
`kutuphaneler/d11_importlari.py` adında bir dizin oluşturduk.

İkinci örnek için de Python'ın standart kütüphanelerinden
`random` ve `math` kullanılacaktır.

Başka bir dosyadan Python kodu çağırmak için import komutunu kullanıyoruz
"""

# Bir kütüphaneyi çekmek için `import` komutunu kullanıp ardından çekmek istediğimiz kütüphaneyi yazarız

# Burada Python'ın standart kütüphanelerinden random kütüphanemizi yazdığımız
# Python dosyası içerisine çektik. Artık bu kütüphaneye bağlı her şeyi kullanabiliriz.
import random

# Eğer bir kütüphaneden sadece bir ya da birkaç içeriği çekmek istersek
# Bu durumda `from {kütüphane_adı} import {istediğimiz içerik}`

# Burada `math` kütüphanesinden `floor` komutunu çağırdık.
# Bu çağırma şeklinde `math` kütüphanesinden `floor` dışında hiçbir içerik gelmez.
# Bu sayede de sisteme daha az yük bindirmiş oluruz.
from math import floor

# Bir kütüphaneden birden fazla içerik çekmek istersek bunu virgül ile ayırarak yapabiliriz.
# Burada `math` kütüphanesinden `sqrt` fonksiyonunu ve `pi` değişkenini çağırdık.
from math import sqrt, pi


# Burada kendi yazdığımız kütüphaneden bir şeyler çağıracağız.

# Kütüphanemiz bir dizin altında olduğu için burada çağırırken {dizin}.{dosya} şeklinde çağırıyoruz.
# dosyayı çağırırken dosya uzantısını kullanmıyoruz.
# Yani `kutuphaneler/d11_importlari.py` dosyası `kutuphaneler.d11_importlari` oluyor
from kutuphaneler.d11_importlari import reverse_string, greet_me

# Bir içeriği çekerken ona dosyamız içerisinde başka bir isim verebiliriz.
# Bu sayede hem bazı senaryolarda anlaşılırlık kolaylaşır, hem de çakışmaları önleriz
# Bunu yapmak için sonuna `as` yazıp ardından yeni adını yazarız
# Bu örnekte kütüphanemizdeki `mahmut` objesi, bu dosya içerisinde `tuncer` adı ile kullanılacaktır
# Bu işlemi `tuncer = mahmut` yazmışız gibi düşünebilirsiniz
from kutuphaneler.d11_importlari import mahmut as tuncer

# Burada `random` kutuphanesi içerisinden `randint` fonksiyonunu çağırdık.
# `randint` bize verdiğimiz aralıkta rastgele bir sayı verir
# Ama burada `random` kütüphanesini komple çağırdığımız için bu kütüphaneye bağlı
# herhangi bir şeyi kullanmak için `random.{çağıracağımız_içerik}` şeklinde kullanmalıyız
print("Rastgele oluşturduğumuz sayı: {}".format(random.randint(1, 20)))

# Burada `math` kütüphanesinden çektiğimiz `floor` fonksiyonunu kullanıyoruz.
# Ayriyetten çektiğimiz için sadece fonksiyonun kendisini yazmamız yeterlidir.
# floor fonksiyonu verdiğimiz float değerinin küsürat kısmını silerek int haline getirir.
print("20.89'un floor fonksiyonundan çıktısı: {}".format(floor(20.89)))

# Burada math kütüphanesinden çektiğimiz pi değerini yazdırıyoruz
# pi, bize pi sayısını verir...
print("Pi sayısı: {}".format(pi))

# Burada math kütüphanesinden çektiğimiz sqrt fonksiyonunu kullanıyoruz
# sqrt fonksiyonu verdiğimiz sayının karekökünü bize verir
print('155 sayisinin karekökü: {}'.format(sqrt(155)))


# Burada yazdığımız `greet_me` fonksiyonuna `mahmut` sözlüğündeki `name` değerini verdik.
greet_result = greet_me(tuncer['name'])
print(greet_result)

# Burada da yazdığımız `reverse_string` fonksiyonuna `mahmut` sözlüğündeki `age` değerini verdik.
print(reverse_string(tuncer['age']))
