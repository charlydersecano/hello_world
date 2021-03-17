# Given a list of numbers
# if number is divisible by 3 print Fizz
# if number is divisible by 5 Buzz
# if number is divisible by 3 and 5 print FizzBuzz
# if number is not divisible by 3, or 5, nor 3 and 5, print the number itself.

import random

numbers = [2, 3, 31, 6, 9, 43, 15, 32, 30, 100, 101, 78, 99]

numero = random.choice(numbers)
if numero  % 3 == 0:
    print('Fizz')
elif numero % 5 == 0:
    print('Buzz')
elif numero % 3 == 0 and numero % 5 == 0:
    print('FizzBuzz')
else:
    print(numero)
