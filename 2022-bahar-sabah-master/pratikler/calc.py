from re import A


def calc(x,y,ops):
    if ops not in "+-*/":
        return "Only +-*/ !!!"
    if ops == "+":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x+y))
    elif ops == "-":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x-y))
    elif ops == "*":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x*y))
    elif ops == "/":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x/y))

while True:

    x = float(input("Please enter first number : "))
    y = float(input("Please enter second number : "))
    ops = input("Please choose calculation type : ")

    print(calc(x,y,ops))



