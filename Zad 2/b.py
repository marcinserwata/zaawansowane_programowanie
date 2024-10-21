# Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę składaną.

def multiply_i(numbers):
    multiplied_numbers = []
    for number in numbers:
        multiplied_numbers.append(number * 2)
    return multiplied_numbers

def multiply_ii(numbers):
    return [number * 2 for number in numbers]

numbers = [1, 2, 3, 4, 5]
print(multiply_i(numbers))
print(multiply_ii(numbers))