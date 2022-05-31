message = "Hello there. My name is Salih Algül"
message = message.upper()
print(message)
message = message.lower()
print(message)
message = message.title()
print(message)
message = message.capitalize()
print(message)

my_message = " Hello there. My name is Salih Algül."
my_message = my_message.strip()
print(my_message)
# my_message = my_message.split(".")
# print(my_message)
print(my_message[:5])
my_message = " ".join(my_message)
print(my_message)
my_message = my_message.split()
print(my_message)
my_message = "-".join(my_message)
print(my_message)

msg = "Hello there. My name is Salih Algül."
# index = msg.find("Salih")
# print(index)   "bize 24 sounucu verir. Yani bu kelime ifadenin içerisinde mevcuttur ve ilk karakter 24 nolu indexe sahiptir."


# print(index)
# index = msg.find("Salihh")

# Bu bize -1 döner. Çünkü Salihh diye bir kelime ifadede yoktur.

isFound = msg.startswith("H")
print(isFound)
isFound = msg.endswith("H")
print(isFound)
msg = msg.replace("Salih", "Yusuf")
msg = msg.replace(" ", "*").replace("ü", "u")
msg = msg.center(100, "-")
print(msg)
