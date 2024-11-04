# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.

def merge_lists(list1, list2):
    merged_list = list1 + list2
    merged_list = list(set(merged_list))
    merged_list = [x ** 3 for x in merged_list]
    return merged_list


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = merge_lists(list1, list2)
print(result)
