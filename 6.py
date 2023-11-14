def a(list1, list2):
    duplicat = []
    for b in list1:
        if b in list2:
            duplicat.append(b)
    return duplicat

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = a(list1, list2)
print(result)