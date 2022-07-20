def get_input_recurrsion(text):
    user_input = input(text + ': ')
    if user_input.isdigit():
        return int(user_input)
    else:
        print("Girdiğiniz içerik bir sayı değildir. Lütfen Tekrar Deneyiniz!")
        return get_input_recurrsion(text)


def get_input_while(text):
    while True:
        user_input = input(text + ': ')
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Girdiğiniz içerik bir sayı değildir. Lütfen Tekrar Deneyiniz!")


input_1 = get_input_while('Bana bir sayi ver abi')
print(input_1)
