# Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

def print_every_second(numbers):
    for i in range(1, len(numbers), 2):
        print(numbers[i])

numbers = list(range(11, 21))
print_every_second(numbers)