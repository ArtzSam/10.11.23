def a(lst):
    result = []
    for i in range(1, len(lst)):

        if lst[i] > max(lst[:i]):

            result.append(lst[i])
    return result

b = input("Введите список элементов через запятую: ")
b = [int(x.strip()) for x in b.split(",")]

result = a(b)
print(result)