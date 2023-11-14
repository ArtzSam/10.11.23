def a(lst):
    element_count = {}
    for element in lst:
        element_count[element] = element_count.get(element, 0) + 1

    least = min(element_count, key=element_count.get)

    return least


spisok = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5]

result = a(spisok)
print(result)