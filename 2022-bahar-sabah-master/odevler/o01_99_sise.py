"""
(x) bottles of beer on the wall. (x) bottles of beer. Take one down, pass it around, (x-1) bottles of beer on the wall.

99 bottles pratiği, gene temel programlama pratiklerinden biridir.
99 ile başlanır, yukarıdaki cümlede x olan kısma 99 yerleştirilir.
Bir noktada sayıdan bir çıkartılıp cümlenin içine yerleştirilir.
Sonraki turda bir çıkartılmış hali ile aynı işlem tekrarlanır.

sayı 1 olduğu andan itibaren cümle içerisindeki "bottles" yazan her yer
sayı bir olacağı için "bottle" olarak değiştirilir.

En son sayı 0'a ulaşınca da "There are no more bottles of beer on the wall!"
yazdırılıp döngü kırılır.

örnek çıktı şuna benzeyecektir:

99 bottles of beer on the wall. 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall. 98 bottles of beer. Take one down, pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall. 97 bottles of beer. Take one down, pass it around, 96 bottles of beer on the wall.
...............
...............
...............
3 bottles of beer on the wall. 3 bottles of beer. Take one down, pass it around, 2 bottles of beer on the wall.
2 bottles of beer on the wall. 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall.
1 bottles of beer on the wall. 1 bottles of beer. Take one down, pass it around, 0 bottle of beer on the wall.
There are no more bottles of beer on the wall!
"""
for i in range(99, 0, -1): for # döngüsü içerisinde belirlenen i verilerinin 99 dan 1 e kadar geriye doğru sayması sağlanır.
    if i > 2: # i verilerinin 2 den büyük olduğu durumlarda if komutundaki sorgular gerçekleşir ve her seferinde aksi (False) olmadıkça döngü başa döner.
        beer = f'{i} bottles of beer'  # beer ve beer_1 eşitlikleri kullanılarak sorgumuza sonuçta kullanabileceği bir veri seti oluşturulur.
        beer_1 = f'{i-1} bottles of beer'
    elif i == 2:               # Döngü içerisindeki tanımlı i sayıları 99'dan geriye sayarken 2 ye geldiğinde if ten sonra gelen ilk elif komut bloğu gerçekleşir.
        beer = f'{i} bottles of beer'     # i nin 2 ye eşit olduğu durumda beer ve beer_1 olarak belirttiğimiz sonuç ekranında kullanılacak olan tanımlamalar için 
        beer_1 = f'{i-1} bottle of beer'    # yeni eşitlik yani ifadelerin nasıl olacağı belirtilmiştir.
    else:
        beer = f'{i} bottle of beer'     # Tüm komut satırlarında döngü içinde sorgulanan bloklar False dönerse yani bu örnekte i ile belirtilen aralıkta dönen sayılar
        beer_1 = f'{i-1} bottle of beer'  # 1 e eşit olduğunda yeni belirlenen beer ve beer_1 deki eşitlikler sonuca yansıyacaktır.
    print(f'{beer} on the wall. {beer}. Take one down, pass it around, {beer_1} on the wall.')  # Bu ifade ile 99 dan 1 e kadar gerçekleşen sayma işleminde 
                                          # ve döngü içerisindeki sayının karşılığı olan sorgulardaki beer ve beer_1 ifadeleri alt alta sonuç ekranında yazdırılır.
print('There are no more bottles of beer on the wall!') # Tüm satırlar ekranda yazdırıldıktan sonra ve döngü kırıldığında ise son satır olarak ekranda belirecek ifadedir.
