"""
match, tıpkı if gibi bir denetleme yapmamız ve ardından istediğimiz kodu
çalıştırmamızı sağlayan bir komuttur.

Match ile if arasındaki fark, if birden fazla kontrol mekanizmasını
beraber yapmanız için verimli iken,
match ise tek bir verinin olası birden fazla sonucunu kontrol etmeniz için
verimli bir yöntemdir.

if içerisinde birden fazla şeyi kontrol edebilirken, match sadece bir şeyin
birden fazla olası sonucunu kontrol eder.

Bu bize çok bir performans kazancı sağlamaz, ama match'in uyduğu senaryolarda
kodumuzun daha kolay yazılası ve anlaşılmasını sağlar.

NOT: Match özelliği Python 3.10 ile birlikte gelmiştir.
"""

user_input = input('Herhangi bir sey gir: ')
user_input = user_input.lower().strip()


match user_input:
    case 'add':
        print('add islemi girildi')
    case 'list':
        print('list islemi girildi')
    case 'deneme':
        print('deneme islemi girildi')
    case _:
        print('Burasi da elsein karsiligi')


# Bu kod yukarıdaki ile aynı işlemi yapar
# if user_input.lower() == 'add':
#     print('add islemi girildi')
# elif user_input.lower() == 'list':
#     print('list islemi girildi')
# elif user_input.lower() == 'deneme':
#     print('deneme islemi girildi')
# else:
#     print('Burasi da elsein karsiligi')
