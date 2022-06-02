string = "abracadabra"
# l = list(string)
# l[5] = "k"
# string = "".join(l)
# print(string)

# string = string[:5] + "k" + string[6:]
# print(string)

def mutate_string(string, position, character):
    return string[:position]+character + string[(position+1):]

