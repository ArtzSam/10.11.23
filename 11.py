def a(n):
    spisok = []
    x = 1
    while x * x <= n:
        y = (n - x * x) ** 0.5
        if int(y) == y:
            spisok.append((x, int(y)))
        print(f" x = {x}: y = {y}")
        x += 1

    return spisok


n = 10

result = a(n)
print(result)