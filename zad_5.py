# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.

def is_value_in_list(list, value):
    return value in list

list = [1, 2, 3, 4, 5]
value = 7
result = is_value_in_list(list, value)
print(result)