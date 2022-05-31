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
