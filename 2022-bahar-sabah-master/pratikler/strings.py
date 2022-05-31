website = "http://www.salihalgul.com"
course = "Python Kursu: Baştan sona 2022 model"

length = len(website)
print(length)
print(len(course))
result = len(course)
print(result)

result = website[7:10]
print(result)

result = website[22:25]
print(result)
result = website[length-3:length]
print(result)

result = course[-22:]
print(result)

# result = course[::2]
result = course[::-1]
print(result)

s = "12345" * 6
print(s)
print(s[::5])
print(s[::7])

name, surname, age, job = "Salih", "Algül", 46, "mühendis"
result = "Benim adım "+ name+ " " + surname+ ", yaşım "+ str(age) + " ve mesleğim "+ job 
print(result)

s = "Hello world"
s = s[0:6] + "W" + s[-4:]
print(s)
s.replace("w","W")
print(s)

result = "abc " * 3
print(result)
