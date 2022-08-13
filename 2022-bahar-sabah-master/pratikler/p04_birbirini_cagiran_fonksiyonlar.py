def get_input(text, is_num=False):
    user_input = input(text + ': ')
    if is_num and user_input.isdigit():
        return int(user_input)
    elif is_num and not user_input.isdigit():
        print('Lütfen bir sayı giriniz!!!!')
        return get_input(text, is_num)
    elif user_input.lower() == 'q':
        exit()
    else:
        return user_input


def create_item_by_user_input():
    name = get_input('Eşyanın Adı')
    stock = get_input('Eşyanın Adedi', is_num=True)
    price = get_input('Eşyanın Fiyatı', is_num=True)

    return {
        'name': name,
        'stock': stock,
        'price': price
    }


while True:
    new_item = create_item_by_user_input()
    print(new_item)
