def a(lst):
    if len(lst) == 0:
        return [[]]
    b = []
    for i in range(len(lst)):

        rest = lst[:i] + lst[i+1:]
        for p in a(rest):

            b.append([lst[i]] + p)
    return b

b1 = [1, 2, 3]
result = a(b1)
print(result)