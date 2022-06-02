# x = 7

# def f(x):

#   res = 5

#   res *= res
#   if x % 2 == 0:

#     print("Sonuc: ", res)

#     return res 
#   else:

#     print("Sonuc: ", res)

#     print(f(4))

# def square(x):
#     res = x * x
#     return res
# square(3)

# def f(x, y = True):

#   if x % 2 == 0:

#     y = False

#   return y
#  f(7,True)

a = 2
def f(x):
    x = 4
    return x
print(f(a))

def kare(x):
    return x * x
def dikdortgen(x, y):
    return x * y
def alanlar_toplami(kare, dikdortgen):
    toplam_alan = kare(2) + dikdortgen(4, 7)
    return toplam_alan
print(toplam_alan)