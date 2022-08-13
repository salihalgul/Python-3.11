from datetime import datetime

with open("yazilan_dosyalar/d11_ilk_ornek.txt", "w") as file:
    out = ""
    for i in range(1, 20):
        out += "merhaba " * i + "\n"
    file.write(out)

with open("yazilan_dosyalar/d11_ilk_ornek.txt", 'w') as mahmut:
    lines = []
    for i in range(20, 0, -1):
        lines.append("lo " * i + "\n")
    mahmut.writelines(lines)

with open('yazilan_dosyalar/d11_ilk_ornek.txt') as file:
    print(file.read())

with open('yazilan_dosyalar/d11_append_ornegi.txt', 'a') as file:
    now = datetime.now()
    file.write(f'Program runned at {now}\n')

with open('yazilan_dosyalar/d11_append_ornegi.txt') as file:
    print(file.read())
