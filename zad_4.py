# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def is_sum_greater_or_equal(a, b, c):
    return a + b >= c


a = 5
b = 3
c = 7
result = is_sum_greater_or_equal(a, b, c)
print(result)
