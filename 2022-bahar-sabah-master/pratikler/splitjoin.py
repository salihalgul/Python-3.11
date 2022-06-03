def split_and_join(line):
    
    return line.replace(' ','*')

if __name__ == '__main__':
    line = input("Bir cümle giriniz : ")
    result = split_and_join(line)
    print("Araya * koydum bak : ", result)