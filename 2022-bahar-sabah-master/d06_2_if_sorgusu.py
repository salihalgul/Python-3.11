a = 12
b = 20
c = 9

if a > b:
    print('a, bden buyuktur')
    print('Bu da calisir')
    print('bu da...')

print('ama bu if sorgusundan bagimsizdir')

if a > c:
    print('a, cden buyuktur')

ornek_list = ['mahmut', 'ibrahim', 'mustafa', 'yildiz']

if 'ali' in ornek_list:
    print('ali ornek listenin icerisinde!')
elif 'mahmut' in ornek_list:
    print('mahmut ornek listenin icerisinde!')
elif 'mustafa' in ornek_list:
    print('mustafa ornek lisenin icerisinde!')


if 12 == 20:
    print('12 ile 20 esit')
else:
    print('12 ile 20nin esit oldugunu kim dusunur?')
