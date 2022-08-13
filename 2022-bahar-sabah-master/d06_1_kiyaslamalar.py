# eşittir: iki tane = işareti ile tanımlanır. İki değer de aynı ise True döner.
"ali" == "veli"  # False
"ali" == "ali"  # True
"ali" == "Ali"  # False
{'ali', 'veli'} == {'veli', 'ali'}  # True
['ali', 'veli'] == ['veli', 'ali']  # False
{'name': 'İsmail', 'surname': 'Türüt'} == {'surname': 'Türüt', 'name': 'İsmail'}  # True


# Eşit değildir: != ile tanımlanır, iki veri birbirinden farklı ise True döner
'ali' != 'veli'  # True
'ali' != 'ali'  # False

# Not: boolean değerleri tersine çevirir
not True  # False
not False  # True

# büyüktür: > işareti ile tanımlanır. ilk değer ikinci değerden büyükse True döner
12 > 20  # False
12 > 12  # False
12 > 9  # True

# Küçüktür: < işareti ile tanımlanır, ilk değer ikinci değerden küçükse True döner
12 < 20  # True
12 < 12  # False
12 < 9  # False

# Büyük eşittir: >= işareti ile tanımlanır. ilk değer ikinci değerden büyük ya da eşitse True döner
12 >= 20  # False
12 >= 12  # True
12 >= 9  # True

# Küçük eşittir: <= işareti ile tanımlanır. İlk değer ikinci değerden küçük ya da eşitse True döner
12 <= 20  # True
12 <= 12  # True
12 <= 9  # False


'ali' in ['ali', 'veli']  # True
'ali' in ['hasan', 'huseyin']  # False
'name' in {'name': 'Mahmut', 'surname': 'Tuncer'}  # True

'ali' not in ['ali', 'veli']  # False
'ali' not in ['hasan', 'huseyin']  # True

a1 = 'ali'
a2 = 'ali'

# is tıpkı == gibi eşitliği kıyaslar. Ancak ram içerisinde birebir aynı veri olup olmadığını sorgular
a1 is a2
a1 == a2


# And: and ile tanımlanır, kendisine verdiğimiz iki boolen değer de True ise True döner

True and True  # True
True and False  # False
False and True  # False
False and False  # False

12 == 12 and 'ali' == 'ali'  # True
12 == 12 and 'ali' == 'veli'  # False
12 > 12 and 'ali' == 'ali'  # False

# Or: or ile tanımlanır. İki boolean değerden sadece biri True olsa bile True döner

True or True  # True
True or False  # True
False or True  # True
False or False  # False

12 == 12 or 'ali' == 'ali'  # True
12 == 12 or 'ali' == 'veli'  # True
12 > 12 or 'ali' == 'ali'  # True
