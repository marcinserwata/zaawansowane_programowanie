# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ),
# a następnie wyświetli jedynie parzyste elementy.

def print_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


numbers = list(range(1, 11))
print_even(numbers)
