from swap import swap_numbers
from extras.desc import print_descending

a = int(input('Enter a number (0-3) for a:'))
b = int(input('Enter a number (0-3) for b:'))
a_str, b_str = swap_numbers(a, b)
print(f'a = {a_str}, b = {b_str}')

num = int(input('Enter a number to print descending:'))
print_descending(num)