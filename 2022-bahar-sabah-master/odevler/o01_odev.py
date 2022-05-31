"""
Örnek çıktı şuna benzeyecektir:

99 bottles of beer on the wall. 99 bottles of beer. Take one down, pass it around, 98 bottles of beer on the wall.
.......
2 bottles of beer on the wall. 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall.
1 bottles of beer on the wall. 1 bottles of beer. Take one down, pass it around, 0 bottle of beer on the wall.
There are no more bottles of beer on the wall!

"""

for i in range(99, -1, -1):
    if i == 2:
        print(f"{2} bottles of beer on the wall. {2} bottles of beer. Take one down, pass it around, {1} bottle of beer on the wall.")
    elif i == 1:
        print(f"{1} bottle of beer on the wall. {1} bottle of beer. Take one down, pass it around, {0} bottle of beer on the wall.")
    elif i == 0:
        print("There are no more bottles of beer on the wall!")    
    else:
        print(f"{i} bottles of beer on the wall. {i} bottles of beer. Take one down, pass it around, {i-1} bottles of beer on the wall.")
