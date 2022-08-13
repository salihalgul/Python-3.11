from json import loads, dumps

envanter = []


def read_from_file():
    with open('pratikler/p05_database.json') as file:
        return loads(file.read())


def write_to_file():
    with open('pratikler/p05_database.json', 'w') as file:
        json_envanter = dumps(envanter)
        file.write(json_envanter)


def get_input(text, is_num=False):
    while True:
        user_input = input(text + ': ')
        if is_num and user_input.isdigit():
            return int(user_input)
        elif is_num:
            print('Aga bana sayı ver!')
        else:
            return user_input


def create_new_item():
    name = get_input('Eşya adı')
    stock = get_input('Stok', is_num=True)
    price = get_input('Fiyat', is_num=True)

    envanter.append({
        'name': name,
        'stock': stock,
        'price': price,
    })
    write_to_file()


def print_item(item, index=None):
    text = f"{item['name']} / {item['price']} / {item['stock']}"
    if index is not None:
        print(f"{index} - {text}")
    else:
        print(text)


def list_items():
    print('index / Ürün Adı / Fiyat / Stok')
    print('-' * 30)
    for index, item in enumerate(envanter):
        print_item(item, index=index)


def main():
    while True:
        task = get_input('Lütfen bir işlem seçiniz. [add, list, quit]')

        if task.lower() == 'add':
            create_new_item()
        elif task.lower() == 'list':
            list_items()
        elif task.lower() == 'quit':
            print('Hoççakaın gidiom ben')
            exit()
        else:
            print('Aga böyle bir komut yok!!!!')


if __name__ == '__main__':
    envanter = read_from_file()
    main()
