def fizz_buzz(number):
    output = ''
    if number % 3 == 0:
        output = 'Fizz'
    if number % 5 == 0:
        output += 'Buzz'
    if not output:
        output = number
    return output


for i in range(1, 51):
    print(fizz_buzz(i))
