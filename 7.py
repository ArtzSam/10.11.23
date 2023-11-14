matrica = [[1, 2, 3], [4, 5, 6], [7, 8, 15]]
n = len(matrica)
a = 0

if n == 2:
    a = matrica[0][0] * matrica[1][1] - matrica[0][1] * matrica[1][0]
    print("Первый блок:")
    print(f"Result: {a}")
else:
    for c in range(n):
        sub_matrica = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != c:
                    row.append(matrica[i][k])
            sub_matrica.append(row)

        sub_calculation = ((sub_matrica[0][0] * sub_matrica[1][1]) - (sub_matrica[0][1] * sub_matrica[1][0]))
        print(f"Блок {c + 1}:")
        print(f"Подсчёт: {sub_matrica}")
        print(f"результат: {sub_calculation}")

        a += ((-1) ** c) * matrica[0][c] * sub_calculation

    print("Окончательный расчет:")
    print(f"Результат: {a}")