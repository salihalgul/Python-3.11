# notlar=[90,72,81,77]
# for e in notlar:
#     print(e)
    
# t = 0
# for e in notlar:
#     t += e
# ortalama = t / len(notlar)
# print("Ortalama", ortalama)


# mailler={"kisi1":"ad1.soyad1@gmail.com","kisi2":"ad2.soyad2@gmail.com","kisi3":"ad3.soyad3@gmail.com"} 
# l=[]

# for v in mailler.values():
#     l.append(v)

# print(",".join(l))

# from re import X


squares=[]
for i in range(1,11):
    squares.append(i*i)
print(squares)

squares = [i*i for i in range(1,11)]
print(squares)

def cube(x):
  return x*x*x
cubes = [cube(x) for x in range(1,11)]
print(cubes)

def squares(x):
  return x*x
squares = [squares(x) for x in range(1,11)]
print(squares)

even_squares = [i for i in squares if i % 2 == 0]
print("even squares:", even_squares)

