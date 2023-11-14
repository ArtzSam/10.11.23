def a(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

sum = 0
for num in range(1, 1001):
    if a(num):
        sum += num
        print(f"Добавление {num} к сумме: {sum}")

print("Финальная сумма:", sum)