counter = 99

while counter <= 99:
    print(f"{counter} bottles of beer on the wall. {counter} bottles of beer. Take one down, pass it around, {counter-1} bottles of beer on the wall.")
    counter -= 1
    if counter == 2:
        print(f"{2} bottles of beer on the wall. {2} bottles of beer. Take one down, pass it around, {1} bottle of beer on the wall.")
        if counter == 1:
            print(f"{1} bottle of beer on the wall. {1} bottle of beer. Take one down, pass it around, {0} bottle of beer on the wall.")
            if counter == 0:
                print("There are no more bottles of beer on the wall!")

                